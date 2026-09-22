from typing import Optional

from api.schemas.quiztoquestion_schemas import QuizToQuestionCreateDTO
from dal.repositories.quiztoquestion_repository import QuizToQuestionRepository

class QuizToQuestionController:
    def __init__(self):
        self.repo = QuizToQuestionRepository()

    def create_Quiz(self, data):
        return self.repo.QuizToQuestionRepository(data)

    def get_byname_question(self, quiz_name):
        return self.repo.get_byname_question(quiz_name)

    def get_byname_answers(self, quiz_name) :
        return self.repo.get_byname_answers(quiz_name)