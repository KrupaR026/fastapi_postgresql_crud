from server.database import base
from sqlalchemy import Column, String, Integer, Boolean, Text, ForeignKey
from server.model.user import User
from server.utils.temp_model import Temp


class Competition(base, Temp):
    __tablename__ = "competition"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(Boolean, default = True)
    description = Column(Text)
    user_id = Column(Integer, ForeignKey(User.id))

