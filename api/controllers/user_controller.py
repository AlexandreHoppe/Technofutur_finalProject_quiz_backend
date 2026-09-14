from typing import Optional

from api.schemas.user_schemas import UserFilterDTO
from dal.repositories.user_repository import UserRepository

class UserController:
    def __init__(self):
        self.repo = UserRepository()

    #Test Get Everything
    def get_all_user(self):
        return self.repo.get_all()