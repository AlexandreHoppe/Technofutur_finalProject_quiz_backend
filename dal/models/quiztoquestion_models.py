from .base_models import Base
from sqlalchemy import Column, ForeignKey, Integer

class QuizToQuestion(Base) :
    __tablename__="QuizToQuestions"
    quiztoquestion_quizId=Column(Integer, ForeignKey("Quizzes.quiz_id"), primary_key=True)
    quiztoquestion_questionId=Column(Integer, ForeignKey("Questions.question_id"), primary_key=True)