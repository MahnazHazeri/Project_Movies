from datetime import datetime
from uuid import UUID

from archipy.models.dtos.base_dtos import BaseDTO
from archipy.models.dtos.pagination_dto import PaginationDTO
from archipy.models.dtos.sort_dto import SortDTO
from pydantic import StrictStr, Field

from src.models.types.movie_sort_type import MovieSortColumnType
from src.schemas.movie import MovieStats

class CreateMovieInputDTOV1(BaseDTO):
    title: StrictStr
    genre: StrictStr | None = None
    release_year: int | None = Field(None, ge=1900, le=2030)
    status: MovieStats


class CreateMovieOutputDTOV1(BaseDTO):
    movie_uuid: UUID

class GetMovieInputDTOV1(BaseDTO):
    movie_uuid: UUID


class GetMovieOutputDTOV1(BaseDTO):
    movie_uuid: UUID
    title: StrictStr
    genre: StrictStr | None = None
    release_year: int | None = None
    status: MovieStats
    rating: int | None = None
    notes: StrictStr | None = None
    created_at: datetime


class MovieItemDTOV1(BaseDTO):
    movie_uuid: UUID
    title: StrictStr
    genre: StrictStr | None = None
    release_year: int | None = None
    status: MovieStats
    rating: int | None = None
    created_at: datetime


class SearchMovieInputDTOV1(BaseDTO):
    title: StrictStr | None = None
    genre: StrictStr | None = None
    status: MovieStats | None = None
    pagination: PaginationDTO
    sort_info: SortDTO[MovieSortColumnType]

    @classmethod
    def create(
        cls,
        title: str | None = None,
        genre: str | None = None,
        status: MovieStats | None = None,
        page: int = 1,
        page_size: int = 10,
        sort_column: MovieSortColumnType = MovieSortColumnType.CREATED_AT,
        sort_order: str = "desc",
    ):
        pagination = PaginationDTO(page=page, page_size=page_size)
        sort_info = SortDTO[MovieSortColumnType](column=sort_column, order=sort_order)

        return cls(
            title=title,
            genre=genre,
            status=status,
            pagination=pagination,
            sort_info=sort_info,
        )

class SearchMovieOutputDTOV1(BaseDTO):
    movies: list[MovieItemDTOV1]
    total: int


class UpdateMovieRestInputDTOV1(BaseDTO):
    title: StrictStr | None = None
    genre: StrictStr | None = None
    release_year: int | None = Field(None, ge=1900, le=2030)
    status: MovieStats | None = None
    rating: int | None = Field(None, ge=1, le=5)
    notes: StrictStr | None = None


class UpdateMovieInputDTOV1(UpdateMovieRestInputDTOV1):
    movie_uuid: UUID

class DeleteMovieInputDTOV1(BaseDTO):
    movie_uuid: UUID


class MovieStatsInputDTOV1(BaseDTO):
    pass


class MovieStatsOutputDTOV1(BaseDTO):
    total_movies: int
    watched_movies: int
    average_rating: float | None = None
