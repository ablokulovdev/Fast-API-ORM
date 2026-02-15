from pydantic import BaseModel


class CommentsListRespons(BaseModel):
    id: int
    text : str | None = None
    author_id : int
    post_id : int
    
    class Config:
        from_attributes = True