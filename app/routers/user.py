from typing import List,Annotated
from fastapi import APIRouter,Path,Query

from app.db.database import LocalSession
from app.models.user import User


from app.schemas.user import UserSearchRespons
user_router = APIRouter(
    prefix="/users",
    tags=["Users Endpoint"]
)


@user_router.get("",response_model=UserSearchRespons)
def get_search(search: Annotated[str | None,Query(min_length=3, max_length=30)]=None):
    
    db = LocalSession()
    
    if search is not None:
        users = db.query(User).filter(User.username.ilike(f"%{search}%")).all()
        
    
        
        return UserSearchRespons(users=users)

    users = db.query(User).all()
    count = db.query(User).count()
    
    return UserSearchRespons(users=users, count=count)


@user_router.get("/{user_id}")
def get_one_user(user_id: Annotated[int,Path(gt=0)]):
    
    db = LocalSession()
    
    users = db.query(User).filter(User.id == user_id).all()
    
    return users

