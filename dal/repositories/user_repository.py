from typing import Optional

from dal.database import get_db
from dal.models.user_models import User

class UserRepository:

    #GetAll
    def get_all(self):
        with get_db() as database:
            users = database.query(User).order_by(User.user_name.desc()).all()
            
            return [
                {
                    "user_id" : user.user_id,
                    "user_name" : user.user_name,
                    "user_password" : user.user_password,
                    "user_email" : user.user_Email
                }
                for user in users
            ]