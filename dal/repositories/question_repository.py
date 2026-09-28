from typing import Optional
import requests, json, html
from dal.database import get_db
from dal.models.question_models import Question
from dal.models.quiz_models import Quiz
from dal.models.quiztoquestion_models import QuizToQuestion


class QuestionRepository:

    #GetAll
    def get_all(self):
        with get_db() as database:
            questions = database.query(Question).order_by(Question.question_id.desc()).all()
            
            return [
                {
                    "question_id" : question.question_id,
                    "question_questions" : question.question_questions,
                    "question_answers" : question.question_answers,
                    "question_category" : question.question_category,
                    "question_type" : question.question_type
                }
                for question in questions
            ]
        
    def get_byname_question(self, quiz_name) :
        with get_db() as database:
            quiz = (
                database.query(Quiz)
                .filter(Quiz.quiz_name == quiz_name)
                .first()
            )

            if quiz is None:
                return None


            questions_text = (
                database.query(Question, Quiz)
                .join(QuizToQuestion, QuizToQuestion.quiztoquestion_questionId == Question.question_id)
                .join(Quiz, QuizToQuestion.quiztoquestion_quizId == Quiz.quiz_id)
                .filter(Quiz.quiz_name == quiz_name)
                .filter(Quiz.quiz_category == Question.question_category)
                .all()
            )

            toBeSend = [
                question.question_questions
                for question, quiz in questions_text
                if quiz.quiz_type in (question.question_type or [])
            ]

            if quiz.quiz_responded >= len(toBeSend):
                return None

            return toBeSend[quiz.quiz_responded]

    def get_byname_answers(self, quiz_name) :
        with get_db() as database:
            quiz = (
                database.query(Quiz)
                .filter(Quiz.quiz_name == quiz_name)
                .first()
            )

            answers_text = (
                database.query(Question, Quiz)
                .join(QuizToQuestion, QuizToQuestion.quiztoquestion_questionId == Question.question_id)
                .join(Quiz, QuizToQuestion.quiztoquestion_quizId == Quiz.quiz_id)
                .filter(Quiz.quiz_name == quiz_name)
                .filter(Quiz.quiz_category == Question.question_category)
                .all()
            )
            toBeSend = [
                (question.question_answers, quiz.quiz_responded, quiz.quiz_length, quiz.quiz_type)
                for question, quiz in answers_text
                if quiz.quiz_type in (question.question_type or [])
            ]

            return toBeSend[quiz.quiz_responded]

    def feed_text_question():

        url = "https://opentdb.com/api.php?amount=50&category=11&difficulty=easy"

        response = requests.get(url).json()
        datas = response.get("results", [])

        datas = html.unescape(datas)
        
        with get_db() as database :
            for data in datas:
                print(data)
                question = Question(
                    question_questions=html.unescape(data.get("question")),
                    question_answers=html.unescape(data.get("correct_answer")),
                    question_category=html.unescape(data.get("category")),
                    question_type=["Text-Mode", "Multiple-Choice"]
                )

                database.add(question)
                database.flush()
 