from typing import Optional

from api.schemas.quiz_schemas import QuizCreateDTO
from dal.repositories.quiz_repository import QuizRepository

class QuizController:
    def __init__(self):
        self.repo = QuizRepository()

    #Test Get Everything
    def get_all_Quiz(self):
        return self.repo.get_all()

    def create_Quiz(self, data):
        return self.repo.QuizRepository(data)
    
    def put_quiz_responded(self, quizName, newResponded) :
        return self.repo.QuizRepository(quizName, newResponded)