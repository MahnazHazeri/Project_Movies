from enum import Enum


class MovieSortColumnType(str, Enum):
    TITLE = "title"
    RELEASE_YEAR = "release_year"
    RATING = "rating"
    CREATED_AT = "created_at"
