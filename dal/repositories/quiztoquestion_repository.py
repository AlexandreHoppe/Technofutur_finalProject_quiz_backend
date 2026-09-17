from typing import Optional

from dal.database import get_db
from dal.models.quiztoquestion import QuizToQuestion

class QuizToQuestionRepository:

    #GetAll
    def get_all(self):
        with get_db() as database:
            quizToQuestions = database.query(QuizToQuestion).order_by(QuizToQuestion.quiz_id.desc()).all()
            
            return [
                {
                    "quiztoquestion_quizId" : quizToQuestion.quiz_id ,
                    "quiztoquestion_questionId" : quizToQuestion.quiz_questionId ,
                }
                for quizToQuestion in quizToQuestions
            ]