from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class File(Base):
    __tablename__ = "file"

    id = Column(Integer, primary_key=True, index=True)
    
    upload = relationship("Upload", back_populates="files")
    