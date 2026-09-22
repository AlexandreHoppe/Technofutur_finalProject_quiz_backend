from flask import Blueprint, jsonify, request
from pydantic import ValidationError

from dal.database import get_db
from dal.models.quiztoquestion_models import QuizToQuestion
from api.controllers.quiztoquestion_controller import QuizToQuestionController
from api.schemas.quiztoquestion_schemas import QuizToQuestionCreateDTO

quiztoquestion_blueprint=Blueprint("quiztoquestions", __name__, url_prefix="/api/quiztoquestions")
quiztoquestion_controller=QuizToQuestionController()

@quiztoquestion_blueprint.route("/<string:quiz_name>/question", methods=["GET"])
def get_byname_question(quiz_name):
    questions = quiztoquestion_controller.get_byname_question(quiz_name)
    return jsonify({
        "data": questions
    }), 200

@quiztoquestion_blueprint.route("<string:quiz_name>/answer", methods=["GET"])
def get_byname_answers(quiz_name):
    answers = quiztoquestion_controller.get_byname_answers(quiz_name)
    return jsonify({
        "data": answers
    })
