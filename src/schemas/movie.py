from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime
from src.models.types_ import MovieStatusType


class BaseMovie(BaseModel):
    title: Optional[str] = None
    genre: Optional[str] = None
    release_year: Optional[int] = Field(None, ge=1900, le=2030)
    rating: Optional[int] = Field(None, ge=1, le=5)
    status: Optional[MovieStatusType] = None
    notes: Optional[str] = None


class MovieCreate(BaseMovie):
    title: str = Field(..., min_length=1)
    status: MovieStatusType

    @field_validator("title")
    @classmethod
    def title_not_empty(cls, v: str):
        if not v.strip():
            raise ValueError("Title must not be empty")
        return v


class MovieUpdate(BaseMovie):
    pass


class MovieResponse(BaseMovie):
    movie_uuid: str
    created_at: datetime

    class Config:
        from_attributes = True


class MovieStats(BaseModel):
    total_movies: int
    watched_movies: int
    average_rating: Optional[float]
