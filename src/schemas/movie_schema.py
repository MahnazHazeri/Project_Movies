from archipy.models.dtos.base_dtos import BaseDTO
from pydantic import BaseModel,Field
from datetime import datetime
from typing import Optional
from src.models.movie_model import StatuseEnum



# new movie -> for input
class MovieCreate(BaseModel):
    title: str
    genre: Optional[str] = None
    release_year: Optional[int] = Field(None, ge=1900, le=2030)
    status: StatuseEnum = Field(..., description="watched|want_to_watch")
    notes: Optional[str] = None
    rating: Optional[int] = Field(None, ge=1, le=5, description="Rating must be between 1 and 5")

# update movie -> for input
class MovieUpdate(BaseModel):
    title: Optional[str] = None
    genre: Optional[str] = None
    release_year: Optional[int] = Field(None, ge=1900, le=2030)
    status: Optional[StatuseEnum] = Field(None, description="watched|want_to_watch")
    notes: Optional[str] = None
    rating: Optional[int] = Field(None, ge=1, le=5, description="Rating must be between 1 and 5")

# Returns the output -> Database output
class MovieResponse(BaseDTO):
    movie_uuid: int
    title: str
    genre: Optional[str] = None
    release_year: Optional[int] = Field(None, ge=1900, le=2030)
    status: StatuseEnum = Field(..., description="watched|want_to_watch")
    notes: Optional[str] = None
    rating: Optional[int] = Field(None, ge=1, le=5, description="Rating must be between 1 and 5")
    created_at: datetime

    class Config:
        orm_mode = True

# Computational/Statistical Output
class MovieStates(BaseDTO):
    total_movies: int
    watched_movies: int
    want_to_watch_movies: int
    average_rating: Optional[float] = None