from pydantic import BaseModel, Field

class QuizCreateDTO(BaseModel):
    quiz_length: int = Field(..., gt=0, lt=100)
    quiz_category: str = Field(..., max_length=100)
    quiz_type: str = Field(..., max_length=100)
    quiz_name: str = Field(max_length=100)