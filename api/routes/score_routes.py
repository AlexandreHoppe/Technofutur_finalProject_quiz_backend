from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from api.controllers.score_controller import ScoreController
from api.schemas.score_schemas import ScoreFilterDTO

score_blueprint= Blueprint("scores", __name__, url_prefix="/api/scores")
score_controller = ScoreController()

@score_blueprint.route("/", methods=['GET'])
def get_all_scores():
    try:
        scores = score_controller.get_all_score()
        return jsonify({
            "data" : scores,
            "count": len(scores)
        }), 200

    except Exception as error :
        return jsonify({"error": str(error)}), 500