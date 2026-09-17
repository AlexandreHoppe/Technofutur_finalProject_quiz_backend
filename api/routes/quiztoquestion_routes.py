from flask import Blueprint, jsonify, request
from pydantic import ValidationError

from dal.database import get_db
from dal.models.quiztoquestion import QuizToQuestion
from api.controllers.quiztoquestion_controller import QuizController
from api.schemas.quiztoquestion_schemas import QuizToQuestionCreateDTO

quiz_blueprint=Blueprint("quizzes", __name__, url_prefix="/api/quiztoquestions")
quiz_controller=QuizController()
