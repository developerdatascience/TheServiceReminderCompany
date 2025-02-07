from sqlalchemy import Integer, Column, String, Boolean, DateTime, ForeignKey
from datetime import datetime
from app.core.database import Base
from sqlalchemy.orm import relationship

class Subscriptions(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    plan = Column(String, default='basic')
    start_date = Column(DateTime, default=datetime.now())
    end_date = Column(DateTime)
    is_active = Column(Boolean, default=False)
    user = Column("User", back_populates='subscriptions')
    
