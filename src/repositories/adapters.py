from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.movie import Movie
from src.models.types_ import MovieStatusType
from src.schemas.movie import MovieCreate, MovieUpdate


class MovieRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_movie(self, data: MovieCreate):
        movie = Movie(**data.model_dump())
        self.session.add(movie)
        await self.session.commit()
        await self.session.refresh(movie)
        return movie

    async def get_movie(self, movie_uuid):
        result = await self.session.execute(
            select(Movie).where(Movie.movie_uuid == movie_uuid)
        )
        return result.scalar_one_or_none()

    async def list_movies(self, status=None, genre=None, rating=None):
        query = select(Movie)

        if status:
            query = query.where(Movie.status == status)
        if genre:
            query = query.where(Movie.genre == genre)
        if rating:
            query = query.where(Movie.rating == rating)

        result = await self.session.execute(query)
        return result.scalars().all()

    async def update_movie(self, movie_uuid, data: MovieUpdate):
        movie = await self.get_movie(movie_uuid)
        if not movie:
            return None

        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(movie, field, value)

        await self.session.commit()
        await self.session.refresh(movie)
        return movie

    async def delete_movie(self, movie_uuid):
        movie = await self.get_movie(movie_uuid)
        if not movie:
            return False

        await self.session.delete(movie)
        await self.session.commit()
        return True

    async def get_stats(self):
        total = await self.session.scalar(select(func.count()).select_from(Movie))

        watched = await self.session.scalar(
            select(func.count()).where(Movie.status == MovieStatusType.WATCHED)
        )

        avg_rating = await self.session.scalar(
            select(func.avg(Movie.rating)).where(Movie.rating.is_not(None))
        )

        return {
            "total_movies": total or 0,
            "watched_movies": watched or 0,
            "average_rating": float(avg_rating) if avg_rating else None,
        }