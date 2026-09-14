from typing import Optional

from api.schemas.quiz_schemas import QuizFilterDTO
from dal.repositories.quiz_repository import QuizRepository

class QuizController:
    def __init__(self):
        self.repo = QuizRepository()

    #Test Get Everything
    def get_all_Quiz(self):
        return self.repo.get_all()