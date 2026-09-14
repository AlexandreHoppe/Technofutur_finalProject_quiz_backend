from typing import Optional

from api.schemas.score_schemas import ScoreFilterDTO
from dal.repositories.score_repository import ScoreRepository

class ScoreController:
    def __init__(self):
        self.repo = ScoreRepository()

    #Test Get Everything
    def get_all_score(self):
        return self.repo.get_all()