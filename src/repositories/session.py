from contextlib import asynccontextmanager
from src.repositories.engine import AsyncSessionFactory


@asynccontextmanager
async def get_session():
    async with AsyncSessionFactory() as session:
        yield session