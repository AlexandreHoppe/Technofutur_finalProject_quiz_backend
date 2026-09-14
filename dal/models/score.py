from .base import Base
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, DateTime

class Score(Base):
    __tablename__="Scores"
    score_id=Column(Integer, primary_key=True, autoincrement=True)
    score_userId=Column(Integer, ForeignKey("Users.user_id"))
    score_quizId=Column(Integer, ForeignKey("Quizzes.quiz_id"))
    score_result=Column(Integer, default=0)
    score_date=Column(DateTime, default=datetime.now, onupdate=datetime.now)