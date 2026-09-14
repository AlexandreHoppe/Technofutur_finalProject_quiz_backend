from contextlib import contextmanager
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

from dal.models.base import Base
from dal.models.user import User
from dal.models.question import Question
from dal.models.quiz import Quiz
from dal.models.score import Score

import os

load_dotenv()
DATABASE_URL= os.getenv("CONNECTION_STRING")

engine = create_engine(DATABASE_URL, echo=False)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db(delete=False):
    if delete:
        Base.metadata.drop_all(bind=engine)
        print("Tables deleted with success.")

    Base.metadata.create_all(bind=engine)
    print("Tables created with success.")

def test_connection():
    try:
        with engine.connect() as connected:
            connected.execute(text("SELECT 1"))
            print("Connected to Database")
            return True
    except Exception as errorMessage:
        print(f"Connection Error : {errorMessage}")
        return False

def seed_data():
    print("This is a test")
    with get_db() as database:
        if database.query(User).count() == 0:
            user = User(
                user_name="Tester Name",
                user_password="TesterPassword1",
                user_Email="testerEmail@email.com"
            )
            database.add(user)
            database.flush()

        if database.query(Question).count() == 0:
            question = Question(
                question_questions="What is yes ?",
                question_answers="Yes",
                question_category="Yes or No",
                question_type="party"
            )
            database.add(question)
            database.flush()

        if database.query(Quiz).count() == 0:
            quiz = Quiz(
                quiz_userId=user.user_id,
                quiz_questionId=question.question_id,
                quiz_responded=2,
                quiz_length=10,
                quiz_type="party"
            )
            database.add(quiz)
            database.flush()

        if database.query(Score).count() == 0:
            score = Score(
                score_userId=user.user_id,
                score_quizId=quiz.quiz_id,
                score_result=2500
            )
            database.add(score)
            database.flush()

        print("Fake data was sent to the database.")

@contextmanager
def get_db():
    database = session_local()
    try:
        yield database
        database.commit()
    except Exception:
        database.rollback()
        raise
    finally:
        database.close()