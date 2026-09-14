from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from api.controllers.user_controller import UserController
from api.schemas.user_schemas import UserFilterDTO

user_blueprint= Blueprint("users", __name__, url_prefix="/api/users")
user_controller = UserController()

@user_blueprint.route("/", methods=['GET'])
def get_all_users():
    try:
        users = user_controller.get_all_user()
        return jsonify({
            "data" : users,
            "count": len(users)
        }), 200

    except Exception as error :
        return jsonify({"error": str(error)}), 500