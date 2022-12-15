from sqlalchemy import Column, DateTime, Boolean
from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID

"""
comman columns of three table
"""


def date_time():
    return datetime.utcnow()


class Temp:
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    is_active = Column(Boolean, default=True)
    is_delete = Column(Boolean, default=False)
    created_at = Column(DateTime, default=date_time())
    updated_at = Column(DateTime, default=date_time())
