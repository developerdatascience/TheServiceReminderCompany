from sqlalchemy import Integer, Column, String, Boolean, DateTime, ForeignKey
from datetime import datetime
from .base import Base

class Email(Base):
    __tablename__ = "emails"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(String)
    sent_at = Column(DateTime, default=datetime.now())
    status = Column(String, default="sent")

