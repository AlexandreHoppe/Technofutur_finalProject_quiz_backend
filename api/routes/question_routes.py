from flask import Blueprint, jsonify, request
from pydantic import ValidationError

from dal.database import get_db
from dal.models.quiztoquestion_models import QuizToQuestion
from api.controllers.question_controller import QuestionController
from api.schemas.quiztoquestion_schemas import QuizToQuestionCreateDTO

question_blueprint=Blueprint("/questions", __name__, url_prefix="/api/questions")
question_controller=QuestionController()

@question_blueprint.route("/", methods=['GET'])
def get_all_quizzes():
    try:
        question = question_controller.get_all_question()
        return jsonify({
            "data" : question,
            "count": len(question)
        }), 200

    except Exception as error :
        return jsonify({"error": str(error)}), 500

@question_blueprint.route("/<string:quiz_name>/question", methods=["GET"])
def get_byname_question(quiz_name):
    questions = question_controller.get_byname_question(quiz_name)
    if questions is None:
        return jsonify({"error": "Quiz not found or no question remains"}), 404
    return jsonify({
        "question": questions
    }), 200

@question_blueprint.route("/<string:quiz_name>/answer", methods=["GET"])
def get_byname_answers(quiz_name):
    answers = question_controller.get_byname_answers(quiz_name)
    return jsonify({
        "answers": answers
    })