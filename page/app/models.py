from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email= Column(String(50), unique=True, index=True)
    name = Column(String(50))
    password = Column(String(255))

    # usedata = relationship("Item", back_populates="user")

class Item(Base):
    __tablename__ = "usedata"

    idx = Column(Integer, primary_key=True, index=True)
    weather = Column(String(10))
    datetime = Column(String(30))
    # owner_id = Column(Integer, ForeignKey("user.id"))
    use = Column(String(35))

    # user = relationship("User", back_populates="usedata")
