from pydantic import BaseModel,Field
from typing import Optional
from src.models import MovieStatus
from uuid import UUID 
from datetime import datetime


class MovieBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=225)
    status: MovieStatus
    release_year: Optional[int] = Field(None, ge=1900, le=2030)
    genre: str | None = None
    rating: int | None = Field(None, ge=1, le=5)
    notes: str | None  = None


class MovieResponse(MovieBase):
      
   movie_uuid: UUID
   created_at: datetime

   class Config:
       from_attributes = True

class MovieStats(BaseModel):
    total_count: int
    watched_count: int
    want_to_watched_count: int
    average_rating: Optional[float] = None

class MovieCreate(MovieBase):
    class Config:
        from_attributes = True

class MovieUpdate(BaseModel):
    title: str | None  = Field(None, min_length=1, max_length=225)
    status: MovieStatus | None  = None
    release_year: int | None = Field(None, ge=1900, le=2030)
    genre: str | None  = None
    rating: int | None = Field(None, ge=1, le=5)
    notes: str | None = None

    class Config:
        from_attributes = True



