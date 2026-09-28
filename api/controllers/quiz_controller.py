from typing import Optional
from flask import jsonify

from api.schemas.quiz_schemas import QuizCreateDTO
from dal.repositories.quiz_repository import QuizRepository

class QuizController:
    def __init__(self):
        self.repo = QuizRepository()

    #Test Get Everything
    def get_all_Quiz(self):
        return self.repo.get_all()

    def create_Quiz(self, data):
        try:       
            required = ["quiz_length", "quiz_category", "quiz_type"]
            missing = [field for field in required if field not in data]
            if missing:
                return jsonify({"error": f"Missing required fields: {missing}"}), 400

            if not isinstance(data["quiz_length"], int) or data["quiz_length"] <= 0:
                return jsonify({"error": "quiz_length must be a positive integer"}), 400



            return jsonify(self.repo.create_Quiz(data)), 201
        except Exception as error :
            return jsonify({"error": str(error)}), 500
    
    def put_quiz_responded(self, quizName, newResponded) :
        try:
            if not isinstance(newResponded, int) or newResponded < 0:
                return jsonify({"error": "quizResponded must be a non-negative integer"}), 400
                
            return jsonify(self.repo.put_quiz_responded(quizName, newResponded)), 200
        except Exception as error:
            return jsonify({"error": str(error)}), 500