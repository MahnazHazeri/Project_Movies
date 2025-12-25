from src.models.dtos import (
    CreateMovieInputDTOV1,
    CreateMovieOutputDTOV1,
    GetMovieInputDTOV1,
    GetMovieOutputDTOV1,
    SearchMovieInputDTOV1,
    SearchMovieOutputDTOV1,
    UpdateMovieInputDTOV1,
    DeleteMovieInputDTOV1,
    MovieStatsInputDTOV1,
    MovieStatsOutputDTOV1,
)
from src.repositories.adapters import MoviePostgresAdapter


class MovieRepository:
    def __init__(self, postgres_adapter: MoviePostgresAdapter):
        self._postgres_adapter: MoviePostgresAdapter = postgres_adapter

    async def create_movie(
        self,
        input_dto: CreateMovieInputDTOV1,
    ) -> CreateMovieOutputDTOV1:
        return await self._postgres_adapter.create_movie(input_dto=input_dto)

    async def get_movie(
        self,
        input_dto: GetMovieInputDTOV1,
    ) -> GetMovieOutputDTOV1:
        return await self._postgres_adapter.get_movie(input_dto=input_dto)

    async def search_movies(
        self,
        input_dto: SearchMovieInputDTOV1,
    ) -> SearchMovieOutputDTOV1:
        return await self._postgres_adapter.search_movies(input_dto=input_dto)

    async def update_movie(
        self,
        input_dto: UpdateMovieInputDTOV1,
    ) -> None:
        await self._postgres_adapter.update_movie(input_dto=input_dto)

    async def delete_movie(
        self,
        input_dto: DeleteMovieInputDTOV1,
    ) -> None:
        await self._postgres_adapter.delete_movie(input_dto=input_dto)

    async def get_movie_stats(
        self,
        input_dto: MovieStatsInputDTOV1,
    ) -> MovieStatsOutputDTOV1:
        return await self._postgres_adapter.get_movie_stats(input_dto=input_dto)
