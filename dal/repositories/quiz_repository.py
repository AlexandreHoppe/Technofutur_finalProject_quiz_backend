from typing import Optional
from flask import jsonify

from dal.database import get_db
from dal.models.quiz_models import Quiz
from dal.models.question_models import Question
from dal.models.quiztoquestion_models import QuizToQuestion

class QuizRepository:

    #GetAll
    def get_all(self):
        with get_db() as database:
            quizzes = database.query(Quiz).order_by(Quiz.quiz_id.desc()).all()
            
            return [
                {
                    "quiz_id" : quiz.quiz_id ,
                    "quiz_UserId" : quiz.quiz_userId ,
                    "quiz_name" : quiz.quiz_name ,
                    "quiz_responce" : quiz.quiz_responded ,
                    "quiz_length" : quiz.quiz_length ,
                    "quiz_done" : quiz.quiz_done ,
                    "quiz_difficulty" : quiz.quiz_difficulty ,
                    "quiz_category" : quiz.quiz_category,
                    "quiz_type" : quiz.quiz_type
                }
                for quiz in quizzes
            ]

    def create_Quiz(self, data):
        print("create_Quiz stated")
        with get_db() as database:
            questions = database.query(Question).filter_by(
                question_category=data["quiz_category"]
            ).limit(data["quiz_length"]).all()
            if not questions:
                return jsonify({"error": "No questions found for this category"}), 400
            
            quiz = Quiz(
                quiz_userId=1,
                quiz_name=data.get("quiz_name"),
                quiz_responded=data.get("quiz_responded", 0),
                quiz_length=data["quiz_length"],
                quiz_done=data.get("quiz_done", False),
                quiz_difficulty=data.get("quiz_difficulty", 0),
                quiz_category=data["quiz_category"],
                quiz_type=data["quiz_type"]
            )

            database.add(quiz)
            database.flush()

            for question in questions:
                database.add(QuizToQuestion(
                    quiztoquestion_quizId=quiz.quiz_id,
                    quiztoquestion_questionId=question.question_id
                ))
            database.flush()

            return {
                "quiz_id": quiz.quiz_id,
                "quiz_userId": quiz.quiz_userId,
                "quiz_name": quiz.quiz_name,
                "quiz_responded": quiz.quiz_responded,
                "quiz_length": quiz.quiz_length,
                "quiz_done": quiz.quiz_done,
                "quiz_difficulty": quiz.quiz_difficulty,
                "quiz_category": quiz.quiz_category,
                "quiz_type": quiz.quiz_type
            }

    def put_quiz_responded(self, quizName, newResponded):
        with get_db() as database:
            quiz = (
                database.query(Quiz).filter(Quiz.quiz_name == quizName).first()
            )
            if quiz is None:
                return jsonify({"error": "Quiz not found"}), 404

            quiz.quiz_responded = newResponded

            if quiz.quiz_responded >= quiz.quiz_length:
                quiz.quiz_done = True

            response = {
                "quiz_name": quiz.quiz_name,
                "quiz_responded": quiz.quiz_responded,
                "quiz_done": quiz.quiz_done
            }