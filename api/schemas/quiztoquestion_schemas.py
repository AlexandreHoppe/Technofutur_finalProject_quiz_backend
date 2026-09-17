from pydantic import BaseModel, Field

class QuizToQuestionCreateDTO(BaseModel):
    quiztoquestion_quizId: int
    quiztoquestion_questionId: int