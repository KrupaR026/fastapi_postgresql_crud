from server.database import base
from sqlalchemy import Column, String, Boolean, Text, ForeignKey
from server.model.user import User
from server.utils.temp_model import Temp
from sqlalchemy.dialects.postgresql import UUID


"""
Create the competition model table
"""


class Competition(base, Temp):
    __tablename__ = "competition"
    name = Column(String)
    status = Column(Boolean, default=True)
    description = Column(Text)
    user_id = Column(UUID, ForeignKey(User.id))
