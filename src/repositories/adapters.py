from sqlalchemy import select, func
from src.models.movie import Movie
from src.models.types_ import MovieStatusType
from src.schemas.movie import MovieStats
from archipy.adapters.postgres.sqlalchemy.adapters import AsyncPostgresSQLAlchemyAdapter


class MoviePostgresAdapter:
    def __init__(self, adapter: AsyncPostgresSQLAlchemyAdapter):
        self._adapter = adapter

    async def create_movie(self, data):
        async with self._adapter.get_session() as db:
            movie = Movie(
                title=data.title,
                genre=data.genre,
                release_year=data.release_year,
                status=data.status.value,
            )
            db.add(movie)
            await db.commit()
            await db.refresh(movie)
            return movie

    async def get_movie(self, movie_uuid):
        async with self._adapter.get_session() as db:
            result = await db.execute(
                select(Movie).where(Movie.movie_uuid == movie_uuid)
            )
            return result.scalar_one_or_none()

    async def update_movie(self, movie_uuid, data):
        async with self._adapter.get_session() as db:
            result = await db.execute(
                select(Movie).where(Movie.movie_uuid == movie_uuid)
            )
            movie = result.scalar_one_or_none()

            if not movie:
                return None

            for key, value in data.model_dump(exclude_unset=True).items():
                if key == "status" and value is not None:
                    setattr(movie, key, value.value)
                else:
                    setattr(movie, key, value)

            await db.commit()
            await db.refresh(movie)
            return movie

    async def delete_movie(self, movie_uuid) -> bool:
        async with self._adapter.get_session() as db:
            result = await db.execute(
                select(Movie).where(Movie.movie_uuid == movie_uuid)
            )
            movie = result.scalar_one_or_none()

            if not movie:
                return False

            await db.delete(movie)
            await db.commit()
            return True

    async def list_movies(self, status=None, genre=None, rating=None):
        async with self._adapter.get_session() as db:
            query = select(Movie)

            if status:
                query = query.where(Movie.status == status)
            if genre:
                query = query.where(Movie.genre == genre)
            if rating:
                query = query.where(Movie.rating == rating)

            result = await db.execute(query)
            return result.scalars().all()

    async def get_stats(self) -> MovieStats:
        async with self._adapter.get_session() as db:
            total = await db.scalar(select(func.count()).select_from(Movie))
            watched = await db.scalar(
                select(func.count()).where(Movie.status == MovieStatusType.WATCHED)
            )
            avg_rating = await db.scalar(
                select(func.avg(Movie.rating)).where(Movie.rating.is_not(None))
            )

            return MovieStats(
                total_movies=total or 0,
                watched_movies=watched or 0,
                average_rating=float(avg_rating) if avg_rating else None,
            )
