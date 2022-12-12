from server.database import base
from sqlalchemy import Column, String, Integer, Date, DateTime, Boolean
from server.utils.temp_model import Temp


class User(base, Temp):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    birth_date = Column(Date)
    gender = Column(String)