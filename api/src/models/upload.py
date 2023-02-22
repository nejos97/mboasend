from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Upload(Base):
    __tablename__ = "upload"

    id = Column(Integer, primary_key=True, index=True)
    is_deleted = Column(Boolean, default=False)

    files = relationship("File", back_populates="upload")