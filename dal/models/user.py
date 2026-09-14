from .base import Base
from sqlalchemy import Column, Integer, String

class User(Base) :
    __tablename__="Users"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(30), nullable=False)
    user_password = Column(String(255), nullable=False)
    user_Email = Column(String(255), nullable=False)