from flask import Blueprint, jsonify, request
from dal.database import get_db
from dal.models.quiz_models import Quiz
from dal.models.quiztoquestion_models import QuizToQuestion
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
    data = request.get_json()
    return quiz_controller.create_Quiz(data)


@quiz_blueprint.route("/<string:quiz_name>/responded", methods=["PUT"])
def put_quiz_responded(quiz_name):
    quiz_responded = request.get_json().get("quizResponded")
    print(quiz_name)
    print(quiz_responded)

    return quiz_controller.put_quiz_responded(quiz_name, quiz_responded)