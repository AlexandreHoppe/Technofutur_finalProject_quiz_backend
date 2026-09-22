from .base_models import Base
from sqlalchemy import Column, Integer, String, Text, JSON

class Question(Base) :
    __tablename__="Questions"
    question_id=Column(Integer, primary_key=True, autoincrement=True)
    question_questions=Column(Text, nullable=False)
    question_answers= Column(Text, nullable=False)
    question_category= Column(String(100), nullable=False)
    question_type= Column(JSON, nullable=False)