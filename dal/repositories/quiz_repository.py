from typing import Optional

from dal.database import get_db
from dal.models.quiz_models import Quiz

class QuizRepository:

    #GetAll
    def get_all(self):
        with get_db() as database:
            quizzes = database.query(Quiz).order_by(Quiz.quiz_id.desc()).all()
            
            return [
                {
                    "quiz_id" : quiz.quiz_id ,
                    "quiz_UserId" : quiz.quiz_userId ,
                    "quiz_name" : quiz.quiz_name ,
                    "quiz_responce" : quiz.quiz_responded ,
                    "quiz_length" : quiz.quiz_length ,
                    "quiz_done" : quiz.quiz_done ,
                    "quiz_difficulty" : quiz.quiz_difficulty ,
                    "quiz_category" : quiz.quiz_category,
                    "quiz_type" : quiz.quiz_type
                }
                for quiz in quizzes
            ]