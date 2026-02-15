from sqlalchemy import URL,create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase

from app.core.config import config


DATABASE_URL = URL.create(
    drivername ="postgresql+psycopg2",
    database = config.DB_NAME,
    username = config.DB_USER,
    password = config.DB_PASS,
    host = config.DB_HOST,
    port = config.DB_PORT
)

engine = create_engine(url=DATABASE_URL,echo=True)

LocalSession = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass


def initital_db():
    from models.user import User
    from models.post import Post
    from models.comment import Comment
    
    Base.metadata.create_all(engine)