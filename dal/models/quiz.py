from .base import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean

class Quiz(Base) :
    __tablename__="Quizzes"
    quiz_id=Column(Integer, primary_key=True, autoincrement=True)
    quiz_userId=Column(Integer, ForeignKey("Users.user_id"))
    quiz_name=Column(String(100))
    quiz_responded=Column(Integer, default=0)
    quiz_length=Column(Integer, nullable=False)
    quiz_done=Column(Boolean, default=False)
    quiz_difficulty=Column(Integer, default=0)
    quiz_category= Column(String(100), nullable=False)
    quiz_type=Column(String(100), nullable=False)
    