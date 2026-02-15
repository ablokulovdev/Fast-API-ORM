from pydantic import BaseModel
from typing import List



class UserListRespons(BaseModel):
    id : int
    first_name : str
    last_name : str | None = None
    username : str
    gender : str
    phone : str | None = None
    
    class Config:
        from_attributes = True
        
        
class UserSearchRespons(BaseModel):
    
    users: List[UserListRespons]
    count: int | None = None
    
    class Config:
        from_attributes = True