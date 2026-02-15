from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey
)
from app.db.database import Base


class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(Integer,primary_key=True,index=True)
    text = Column(Text)
    author_id = Column(ForeignKey("users.id"),nullable=False)
    post_id = Column(ForeignKey("posts.id"),nullable=False)
    
    # user = relationship("User", back_populates="comments")
    # post = relationship("Post", back_populates="comments")
    
    def __repr__(self):
        return f"Comment( id = {self.id}, text = {self.text}, author_id = {self.author_id}, post_id = {self.post_id})"