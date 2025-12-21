from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from archipy.models.entities.sqlalchemy.base_entities import BaseEntity




DATABASE_URL = "postgresql+asyncpg://movie_admin:245567@localhost:5432/movie_db"

engine = create_async_engine(
    DATABASE_URL,
    echo = True
)

SessionLocal = async_sessionmaker(
    bind = engine,
    expire_on_commit=False
)

Base = BaseEntity

async def get_db():
    async with SessionLocal() as db:
        yield db

    