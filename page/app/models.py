from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "test"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)