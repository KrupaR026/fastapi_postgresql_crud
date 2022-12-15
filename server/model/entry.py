from server.database import base
from sqlalchemy import Column, String, ForeignKey
from server.model.competition import Competition
from server.utils.temp_model import Temp
from sqlalchemy.dialects.postgresql import UUID

"""
Create the entry model table
"""


class Entry(base, Temp):
    __tablename__ = "entry"
    title = Column(String)
    topic = Column(String)
    state = Column(String)
    country = Column(String)
    competition_id = Column(UUID, ForeignKey(Competition.id))
