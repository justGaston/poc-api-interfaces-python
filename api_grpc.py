from concurrent import futures
import grpc
from user_pb2 import User, UserList, Empty
import user_pb2_grpc
from user_api_interface import userAPIInterface

class ApiGrpc(userAPIInterface, user_pb2_grpc.UserServiceServicer):
    def __init__(self):
        self.users = []

    def get_list_users(self, request, context):
        return UserList(users=self.users)

    def create_user(self, request, context):
        user = User(id=request.id, name=request.name)
        self.users.append(user)
        return user

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(ApiGrpc(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("start server")
    server.wait_for_termination()
