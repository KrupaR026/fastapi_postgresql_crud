from sqlalchemy import Column, String, Integer, Date, DateTime, Boolean
from datetime import datetime


class Temp():
    is_active = Column(Boolean, default = True)
    is_delete = Column(Boolean, default = False)
    created_at = Column(DateTime, default = datetime.utcnow)
    updated_at = Column(DateTime, default = datetime.utcnow)
