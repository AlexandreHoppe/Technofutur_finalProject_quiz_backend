from .base import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean

class Quiz(Base) :
    __tablename__="Quizzes"
    quiz_id=Column(Integer, primary_key=True, autoincrement=True)
    quiz_userId=Column(Integer, ForeignKey("Users.user_id"))
    quiz_questionId=Column(Integer, ForeignKey("Questions.question_id"))
    quiz_responded=Column(Integer, default=0)
    quiz_length=Column(Integer, nullable=False)
    quiz_state=Column(Boolean, default=False)
    quiz_difficulty=Column(Integer, default=0)
    quiz_type=Column(String(100), nullable=False)
    