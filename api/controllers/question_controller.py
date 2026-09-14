from typing import Optional

from api.schemas.question_schemas import QuestionFilterDTO
from dal.repositories.question_repository import QuestionRepository

class QuestionController:
    def __init__(self):
        self.repo = QuestionRepository()

    #Test Get Everything
    def get_all_question(self):
        return self.repo.get_all()