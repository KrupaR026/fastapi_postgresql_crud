from server.database import base
from sqlalchemy import Column, String, Integer, ForeignKey
from server.model.competition import Competition
from server.utils.temp_model import Temp


# Create the entry model table
class Entry(base, Temp):
    __tablename__ = "entry"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    topic = Column(String)
    state = Column(String)
    country = Column(String)
    competition_id = Column(Integer, ForeignKey(Competition.id))
