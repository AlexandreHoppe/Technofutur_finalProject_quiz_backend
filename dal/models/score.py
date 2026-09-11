from .base import Base
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, DateTime

class Score(Base):
    score_Id=Column(Integer, primary_key=True, autoincrement=True)
    score_UserId=Column(Integer, ForeignKey("User.user_id"))
    score_QuizId=Column(Integer, ForeignKey("Quiz.quiz_id"))
    score_Result=Column(Integer, default=0)
    score_Date=Column(DateTime, default=datetime.now, onupdate=datetime.now)