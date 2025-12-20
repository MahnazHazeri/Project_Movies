from src.repositories.movie_repo import MovieRepository
from sqlalchemy.future import select
from src.models import Movie,MovieStatus
from uuid import UUID


class MovieOperation:
    def __init__(self, repository: MovieRepository) -> None:
        self.repository = repository

    async def create(self, **data) -> Movie:
        new_movie = Movie(**data)
        movie = await self.repository.add(new_movie)
        try:
            await self.repository.session.commit()
            await self.repository.session.refresh(movie)
            return movie
        except Exception as e:
            await self.repository.session.rollback()
            raise e
    
    async def get_movie_by_id(self, movie_uuid:UUID) -> Movie:
        movie = await self.repository.get_by_id(movie_uuid)
        if not movie:
            raise ValueError(f"Movie with id{movie_uuid} not found!")
        return movie
