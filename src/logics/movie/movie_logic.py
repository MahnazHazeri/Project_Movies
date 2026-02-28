from fastapi import HTTPException


class MovieLogic:

    def __init__(self, movie_repository):
        self.movie_repository = movie_repository

    async def create_movie(self, data):
        return await self.movie_repository.create_movie(data)

    async def get_movie(self, movie_uuid):
        movie = await self.movie_repository.get_movie(movie_uuid)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        return movie

    async def list_movies(self, status=None, genre=None, rating=None):
        return await self.movie_repository.list_movies(status, genre, rating)

    async def update_movie(self, movie_uuid, data):
        movie = await self.movie_repository.update_movie(movie_uuid, data)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        return movie

    async def delete_movie(self, movie_uuid):
        deleted = await self.movie_repository.delete_movie(movie_uuid)
        if not deleted:
            raise HTTPException(status_code=404, detail="Movie not found")

    async def get_stats(self):
        return await self.movie_repository.get_stats()