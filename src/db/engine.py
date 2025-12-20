from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase,MappedAsDataclass
from archipy.configs.base_config import BaseConfig


config = BaseConfig.global_config()

DATABASE_URL = "postgresql+asyncpg://movie_admin:245567@localhost:5432/movie_db"

engine = create_async_engine(
    DATABASE_URL,
    echo = True
)

SessionLocal = async_sessionmaker(
    bind = engine,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with SessionLocal() as db:
        yield db

    