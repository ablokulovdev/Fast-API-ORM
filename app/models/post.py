from sqlalchemy import (
    Column,
    String,
    Integer,
    Text,
    ForeignKey
)
from sqlalchemy.orm import relationship


from db.database import Base

class Post(Base):
    
    __tablename__  = "posts"
    
    id = Column(Integer,primary_key=True)
    title = Column(String(50),nullable=False)
    description = Column(Text)
    author_id = Column(ForeignKey("users.id"),nullable=False)
    
    user = relationship("User",back_populates="posts")
    comments = relationship("Comment",back_populates="post",cascade="all, delete-orphan")
    
    
    def __repr__(self):
        return f"Post( id = {self.id}, title = {self.title}, description = {self.description}, author_id = {self.author_id})"
    
    