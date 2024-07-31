from user_api_interface import userAPIInterface
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List



app = FastAPI()

class User(BaseModel):
    id: int
    name: str

class ApiFastAPI(userAPIInterface):
    
    def __init__(self):
        self.users = []
    
    def get_list_users(self):
        @app.get("/users", response_model=List[User])
        def get_users():
            return self.users
    
    def create_user(self):
        @app.post("/users", response_model=User)
        def create_user(user: User):
            self.users.append(user)
            return user
