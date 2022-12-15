from server.database import base
from sqlalchemy import Column, String, Date
from server.utils.temp_model import Temp

"""
Create the user model table
"""


class User(base, Temp):
    __tablename__ = "user"
    name = Column(String)
    birth_date = Column(Date)
    gender = Column(String)
