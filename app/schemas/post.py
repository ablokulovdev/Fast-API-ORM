from pydantic import BaseModel



class PostsListRespons(BaseModel):
    id : int
    title : str
    description: str | None = None
    author_id : int
    
    
    class Config:
        from_attributes = True