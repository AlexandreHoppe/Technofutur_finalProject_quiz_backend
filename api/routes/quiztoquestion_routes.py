from flask import Blueprint, jsonify, request
from pydantic import ValidationError

from dal.database import get_db
from dal.models.quiztoquestion_models import QuizToQuestion
from api.controllers.quiztoquestion_controller import QuizToQuestionController
from api.schemas.quiztoquestion_schemas import QuizToQuestionCreateDTO

quiztoquestion_blueprint=Blueprint("quiztoquestions", __name__, url_prefix="/api/quiztoquestions")
quiztoquestion_controller=QuizToQuestionController()

@quiztoquestion_blueprint.route("/<string:quiz_name>/<int:question_number>/question", methods=["GET"])
def get_byname_question(quiz_name, question_number):
    questions = quiztoquestion_controller.get_byname_question(quiz_name)
    if question_number >= len(questions):
        return jsonify({"error": "Question number does not exist"}), 404
    return jsonify({
        "data": questions[question_number]
    }), 200

@quiztoquestion_blueprint.route("<string:quiz_name>/<int:question_number>/answer", methods=["GET"])
def get_byname_answers(quiz_name, question_number):
    answers = quiztoquestion_controller.get_byname_answers(quiz_name)
    if question_number >= len(answers):
        return jsonify({"error": "Answer number does not exist"}), 404
    return jsonify({
        "data": answers[question_number]
    })
