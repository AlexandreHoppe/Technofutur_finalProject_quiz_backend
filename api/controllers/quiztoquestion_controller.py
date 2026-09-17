from typing import Optional

from api.schemas.quiztoquestion_schemas import QuizToQuestionCreateDTO
from dal.repositories.quiztoquestion_repository import QuizToQuestionRepository

class QuizController:

    def create_Quiz(self, data):
        return self.repo.QuizToQuestionRepository(data)