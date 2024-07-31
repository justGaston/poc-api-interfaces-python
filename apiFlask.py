from flask import Flask, jsonify, request
from user_api_interface import userAPIInterface

app = Flask(__name__)

class ApiFlask(userAPIInterface):
    
    def __init__(self):
        self.users = []
    
    def get_list_users(self):
        @app.route('/users', methods=['GET'])
        def get_users():
            return jsonify(self.users), 200
    
    def create_user(self):
        @app.route('/users', methods=['POST'])
        def create_user():
            user = request.json
            self.users.append(user)
            return jsonify(user), 201
