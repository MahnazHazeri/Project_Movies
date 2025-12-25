from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = "postgresql+asyncpg://postgres:1234@localhost:5432/movies_db"

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
)
