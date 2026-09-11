from .base import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean

class Quiz(Base) :
    __tablename__="Quiz"
    quiz_id=Column(Integer, primary_key=True, autoincrement=True)
    quiz_UserId=Column(Integer, ForeignKey("User.user_id"))
    quiz_questionId=Column(Integer, ForeignKey("Question.question_id"))
    quiz_responce=Column(Integer, default=0)
    quiz_length=Column(Integer, nullable=False)
    quiz_state=Column(Boolean, default=False)
    quiz_difficulty=Column(Integer, default=0)
    quiz_type=Column(String(100), nullable=False)
    