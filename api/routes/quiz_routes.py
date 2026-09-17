from flask import Blueprint, jsonify, request
from dal.database import get_db
from dal.models.quiz_models import Quiz
from dal.models.quiztoquestion_models import QuizToQuestion
from dal.models.question_models import Question
from api.controllers.quiz_controller import QuizController
from api.controllers.question_controller import QuestionController

quiz_blueprint=Blueprint("quizzes", __name__, url_prefix="/api/quizzes")
quiz_controller=QuizController()
questionController=QuestionController()

@quiz_blueprint.route("/", methods=['GET'])
def get_all_quizzes():
    try:
        quizzes = quiz_controller.get_all_Quiz()
        return jsonify({
            "data" : quizzes,
            "count": len(quizzes)
        }), 200

    except Exception as error :
        return jsonify({"error": str(error)}), 500



@quiz_blueprint.route("/", methods=["POST"])
def create_quiz():
    try:
        data = request.get_json()

        required = ["quiz_length", "quiz_category", "quiz_type"]
        missing = [field for field in required if field not in data]
        if missing:
            return jsonify({"error": f"Missing required fields: {missing}"}), 400

        if not isinstance(data["quiz_length"], int) or data["quiz_length"] <= 0:
            return jsonify({"error": "quiz_length must be a positive integer"}), 400

        with get_db() as db:
            questions = db.query(Question).filter_by(
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

            db.add(quiz)
            db.flush()

            for question in questions:
                db.add(QuizToQuestion(
                    quiztoquestion_quizId=quiz.quiz_id,
                    quiztoquestion_questionId=question.question_id
                ))
            db.flush()

            created = {
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

        return jsonify(created), 201
    except Exception as error :
        return jsonify({"error": str(error)}), 500