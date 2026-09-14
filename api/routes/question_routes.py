from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from api.controllers.question_controller import QuestionController
from api.schemas.question_schemas import QuestionFilterDTO

question_blueprint= Blueprint("questions", __name__, url_prefix="/api/questions")
question_controller = QuestionController()

@question_blueprint.route("/", methods=['GET'])
def get_all_questions():
    try:
        questions = question_controller.get_all_question()
        return jsonify({
            "data" : questions,
            "count": len(questions)
        }), 200

    except Exception as error :
        return jsonify({"error": str(error)}), 500