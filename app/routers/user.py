from typing import Annotated

from fastapi import APIRouter,Path,Query

from app.db.database import LocalSession
from app.models.user import User


from app.schemas.user import UserSearchRespons
user_router = APIRouter(
    prefix="/users",
    tags=["Users Endpoint"]
)


@user_router.get("",response_model=UserSearchRespons)
def get_search(
    search: Annotated[str | None,Query(min_length=3, max_length=30)]=None,
    page : Annotated[int ,Query(ge=1)]=1,
    limit : Annotated[int, Query(ge=1, le=100)]=10
    ):
    
    db = LocalSession()
    
    if search is not None:
        users = db.query(User).filter(User.username.ilike(f"%{search}%")).all()
        return UserSearchRespons(users=users)
    
    offset = (page-1) * limit
    users = db.query(User).offset(offset).limit(limit).all()

    
    count = db.query(User).count()
    
    return UserSearchRespons(users=users, count=count)


@user_router.get("/{user_id}")
def get_one_user(user_id: Annotated[int,Path(gt=0)]):
    
    db = LocalSession()
    
    users = db.query(User).filter(User.id == user_id).all()
    
    return users


@user_router.post("")
def add_users():
    return {
        "detail": "user qo'shildi"
    }