from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from src.models.movie import Movie
from src.models.types_ import MovieStatusType
from src.schemas.movie import MovieStats
from src.schemas.movie import MovieCreate, MovieUpdate

class MovieLogic:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def create_movie(self, data: MovieCreate) -> Movie:
        movie = Movie(
            title=data.title,
            genre=data.genre,
            release_year=data.release_year,
            status=data.status.value,
        )
        self.db.add(movie)
        await self.db.commit()
        await self.db.refresh(movie)
        return movie

    async def get_movie(self, movie_uuid) -> Movie | None:
        result = await self.db.execute(
            select(Movie).where(Movie.movie_uuid == movie_uuid)
        )
        return result.scalar_one_or_none()

    async def update_movie(self, movie_uuid, data: MovieUpdate) -> Movie | None:
        movie = await self.get_movie(movie_uuid)
        if not movie:
            return None

        for key, value in data.model_dump(exclude_unset=True).items():
            if key == "status" and value is not None:
                setattr(movie, key, value.value)
            else:
                setattr(movie, key, value)

        await self.db.commit()
        await self.db.refresh(movie)
        return movie

    async def delete_movie(self, movie_uuid) -> bool:
        movie = await self.get_movie(movie_uuid)
        if not movie:
            return False

        await self.db.delete(movie)
        await self.db.commit()
        return True

    async def list_movies(self, status=None, genre=None, rating=None) -> list[Movie]:
        query = select(Movie)
        if status:
            query = query.where(Movie.status == status)
        if genre:
            query = query.where(Movie.genre == genre)
        if rating:
            query = query.where(Movie.rating == rating)

        result = await self.db.execute(query)
        return result.scalars().all()

    async def get_stats(self) -> MovieStats:
        total = await self.db.scalar(select(func.count()).select_from(Movie))
        watched = await self.db.scalar(
            select(func.count()).where(Movie.status == MovieStatusType.WATCHED)
        )
        avg_rating = await self.db.scalar(
            select(func.avg(Movie.rating)).where(Movie.rating.is_not(None))
        )
        return MovieStats(
            total_movies=total or 0,
            watched_movies=watched or 0,
            average_rating=float(avg_rating) if avg_rating else None,
        )
