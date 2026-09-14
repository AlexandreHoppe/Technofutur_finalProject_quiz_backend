from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from api.controllers.quiz_controller import QuizController
from api.schemas.quiz_schemas import QuizFilterDTO

quiz_blueprint= Blueprint("quizzes", __name__, url_prefix="/api/quizzes")
quiz_controller = QuizController()

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