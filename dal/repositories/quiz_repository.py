from typing import Optional

from dal.database import get_db
from dal.models.quiz import Quiz

class QuizRepository:

    #GetAll
    def get_all(self):
        with get_db() as database:
            quizzes = database.query(Quiz).order_by(Quiz.quiz_id.desc()).all()
            
            return [
                {
                    "quiz_id" : quiz.quiz_id ,
                    "quiz_UserId" : quiz.quiz_userId ,
                    "quiz_questionId" : quiz.quiz_questionId ,
                    "quiz_responce" : quiz.quiz_responded ,
                    "quiz_length" : quiz.quiz_length ,
                    "quiz_state" : quiz.quiz_state ,
                    "quiz_difficulty" : quiz.quiz_difficulty ,
                    "quiz_type" : quiz.quiz_type
                }
                for quiz in quizzes
            ]