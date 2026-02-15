from fastapi import APIRouter
from typing import List

from app.db.database import LocalSession
from app.models.comment import Comment
from app.schemas.comment import CommentsListRespons


comment_router = APIRouter(
    prefix="/comments",
    tags=["Comments Endpointlar"]
)


@comment_router.get("",response_model=List[CommentsListRespons])
def get_comment():
    
    db = LocalSession()
    
    return db.query(Comment).all()