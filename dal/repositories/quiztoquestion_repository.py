from typing import Optional

from dal.database import get_db
from dal.models.question_models import Question
from dal.models.quiz_models import Quiz
from dal.models.quiztoquestion_models import QuizToQuestion

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

    def get_byname_question(self, quiz_name) :
        with get_db() as database:
            quiz = (
                database.query(Quiz)
                .filter(Quiz.quiz_name == quiz_name)
                .first()
            )

            questions_text = (
                database.query(Question, Quiz)
                .join(QuizToQuestion, QuizToQuestion.quiztoquestion_questionId == Question.question_id)
                .join(Quiz, QuizToQuestion.quiztoquestion_quizId == Quiz.quiz_id)
                .filter(Quiz.quiz_name == quiz_name)
                .filter(Quiz.quiz_category == Question.question_category)
                .filter(Quiz.quiz_category == Question.question_category)
                .all()
            )
            toBeSend = [
                question.question_questions
                for question, quiz in questions_text
                if quiz.quiz_type in (question.question_type or [])
            ]

            return toBeSend[quiz.quiz_responded]

    def get_byname_answers(self, quiz_name) :
        with get_db() as database:
            answers_text = (
                database.query(Question, Quiz)
                .join(QuizToQuestion, QuizToQuestion.quiztoquestion_questionId == Question.question_id)
                .join(Quiz, QuizToQuestion.quiztoquestion_quizId == Quiz.quiz_id)
                .filter(Quiz.quiz_name == quiz_name)
                .filter(Quiz.quiz_category == Question.question_category)
                .all()
            )
            return [
                question.question_answers
                for question, quiz in answers_text
                if quiz.quiz_type in (question.question_type or [])
            ]