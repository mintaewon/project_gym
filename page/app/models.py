from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "test"

    id = Column(String(50), primary_key=True, index=True)
    name = Column(String(50), index=True)
    password = Column(String(255))