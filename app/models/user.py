from sqlalchemy import (
    Column,
    Integer,
    String
)
from sqlalchemy.orm import relationship
from db.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True)
    first_name = Column(String(50),nullable=False)
    last_name = Column(String(50))
    username = Column(String(50),unique=True,nullable=False)
    gender = Column(String(50),nullable=False)
    phone = Column(String(50))
    
    posts = relationship("Post", back_populates="user",cascade="all, delete-orphan")
    comments = relationship("Comment", back_populates="user",cascade="all, delete-orphan")
    
    
    def __repr__(self):
        return f"id = {self.id},first_name = {self.first_name}, last_name = {self.last_name}, username = {self.username}, phone = {self.phone} "