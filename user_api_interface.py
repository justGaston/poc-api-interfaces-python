from abc import ABC, abstractmethod

class userAPIInterface(ABC):
    
    @abstractmethod
    def get_list_users(self):
        pass
    
    @abstractmethod
    def create_user(self):
        pass
