from src.schemas.movie import MovieCreate, MovieUpdate, MovieStats

class MovieLogic:
    def __init__(self, movie_repository):
        self.movie_repository = movie_repository

    async def create_movie(self, data: MovieCreate):
        return await self.movie_repository.create_movie(data)

    async def get_movie(self, movie_uuid):
        return await self.movie_repository.get_movie(movie_uuid)

    async def update_movie(self, movie_uuid, data: MovieUpdate):
        return await self.movie_repository.update_movie(movie_uuid, data)

    async def delete_movie(self, movie_uuid) -> bool:
        return await self.movie_repository.delete_movie(movie_uuid)

    async def list_movies(self, status=None, genre=None, rating=None):
        return await self.movie_repository.list_movies(
            status=status,
            genre=genre,
            rating=rating,
        )

    async def get_stats(self) -> MovieStats:
        return await self.movie_repository.get_stats()
