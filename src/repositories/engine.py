import os
from sqlalchemy.ext.asyncio import create_async_engine


DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql+asyncpg://postgres:1234@db:5432/mydb"
)

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
)