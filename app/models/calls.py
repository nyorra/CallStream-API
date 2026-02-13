from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base


class Calls(Base):
    __tablename__ = "calls"

    id = Column(Integer, primary_key=True, index=True)
    call_id = Column(String(32), unique=True, index=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    phone_number = Column(String(12), index=True, nullable=False)
    call_type = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
