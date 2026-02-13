from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base


class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    call_id = Column(
        String(32),
        ForeignKey("calls.call_id", ondelete="CASCADE"),
        unique=True,
        index=True,
        nullable=False
    )
    file_path = Column(String, nullable=False)
    file_size = Column(Integer, nullable=True)
    file_format = Column(String(10), default="mp3")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
