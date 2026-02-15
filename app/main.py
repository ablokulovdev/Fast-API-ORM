from fastapi import FastAPI
from app.routers.user import user_router
from app.routers.post import post_router
from app.routers.comment import comment_router

app = FastAPI(title="Blog API")


app.include_router(user_router)
app.include_router(post_router)
app.include_router(comment_router)