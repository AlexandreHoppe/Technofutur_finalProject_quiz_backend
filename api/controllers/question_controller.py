from typing import Optional
from flask import jsonify


from api.schemas.question_schemas import QuestionFilterDTO
from dal.repositories.question_repository import QuestionRepository

class QuestionController:
    def __init__(self):
        self.repo = QuestionRepository()

    #Test Get Everything
    def get_all_question(self):
        return self.repo.get_all()

    def create_Quiz(self, data):
        return self.repo.QuizToQuestionRepository(data)
    
    def get_byname_question(self, quiz_name):

        questions = self.repo.get_byname_question(quiz_name)
        
        if questions is None:
                return jsonify({"error": "Quiz not found or no question remains"}), 404
        return jsonify({
            "question": questions
        }), 200 
    
    def get_byname_answers(self, quiz_name) :
        answers = self.repo.get_byname_answers(quiz_name)
        return jsonify({
            "answers": answers
        })