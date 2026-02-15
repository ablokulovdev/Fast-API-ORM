from fastapi import APIRouter,Query,Path
from typing import List, Annotated

from app.db.database import LocalSession
from app.models.post import Post
from app.schemas.post import PostsListRespons
from app.models.post import Post

post_router = APIRouter(
    prefix="/posts",
    tags=["Posts Endpoint"]
)

@post_router.get("",response_model=List[PostsListRespons])
def get_search(search: Annotated[str | None, Query(min_length=3,max_length=50)]=None):
    
    db = LocalSession()
    
    if search is not None:
        posts = db.query(Post).filter(Post.title.ilike(f"%{search}%")).all()
        
        return posts

    posts = db.query(Post).all()
    
    return posts
    
    
@post_router.get("/{post_id}",response_model=List[PostsListRespons])
def get_posts(post_id: Annotated[int,Path(gt=0)]):
    
    db = LocalSession()
    
    posts = db.query(Post).filter(Post.id == post_id).all()
    
    return posts
    
    