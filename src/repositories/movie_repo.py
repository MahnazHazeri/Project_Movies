from sqlalchemy.ext.asyncio import AsyncSession
from  sqlalchemy.future import select
from src.models import Movie
from uuid import UUID


class MovieRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, movie_uuid:UUID) -> Movie | None:
        query = select(Movie).where(Movie.movie_uuid == movie_uuid)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
    

    async def add(self, movie:Movie) -> Movie:
        self.session.add(movie)
        return movie
    