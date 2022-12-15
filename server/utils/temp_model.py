from sqlalchemy import Column, DateTime, Boolean
from datetime import datetime

"""
comman columns of three table
"""


def date_time():
    return datetime.utcnow()


class Temp:
    is_active = Column(Boolean, default=True)
    is_delete = Column(Boolean, default=False)
    created_at = Column(DateTime, default=date_time())
    updated_at = Column(DateTime, default=date_time())
