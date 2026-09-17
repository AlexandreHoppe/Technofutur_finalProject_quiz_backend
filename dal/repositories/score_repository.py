from typing import Optional

from dal.database import get_db
from dal.models.score_models import Score

class ScoreRepository:

    #GetAll
    def get_all(self):
        with get_db() as database:
            scores = database.query(Score).order_by(Score.score_id.desc()).all()

            return [
                {
                    "score_id" : score.score_id,
                    "score_userId" : score.score_userId,
                    "score_quizId" : score.score_quizId,
                    "score_result" : score.score_result,
                    "score_date" : score.score_date
                }
                for score in scores
            ]