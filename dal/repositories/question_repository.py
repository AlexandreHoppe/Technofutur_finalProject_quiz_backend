from typing import Optional

from dal.database import get_db
from dal.models.question_models import Question

class QuestionRepository:

    #GetAll
    def get_all(self):
        with get_db() as database:
            questions = database.query(Question).order_by(Question.question_id.desc()).all()
            
            return [
                {
                    "question_id" : question.question_id,
                    "question_questions" : question.question_questions,
                    "question_answers" : question.question_answers,
                    "question_category" : question.question_category,
                    "question_type" : question.question_type
                }
                for question in questions
            ]