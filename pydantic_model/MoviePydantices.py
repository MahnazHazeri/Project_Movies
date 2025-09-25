from pydantic import BaseModel,Field
from fastapi import Path
from datetime import datetime
from models import statusEnum 

class MovieCreate(BaseModel):
    title: str
    genre: str | None
    release_year: int | None = Field(None ,ge = 1900 , le = 2030)
    status_: statusEnum  = Field(..., description="watched|want_to_watch")
    notes: str | None


class MovieUpdate(BaseModel):
    title: str | None
    genre: str | None
    release_year: int | None
    status_: statusEnum  = Field(..., description="watched|want_to_watch")
    notes: str | None


    
class MovieResponse(BaseModel):
    movie_uuid = int
    title:str
    genre: str | None
    release_year: int | None = Field(None ,ge = 1900 , le = 2030)
    status_: statusEnum  = Field(..., description="watched|want_to_watch")
    notes: str | None
    rating: int | None
    created_at = datetime


class MovieStats(BaseModel):
    total_movies: int
    watched_movies: int
    want_to_watch_movies: int
    average_rating: float | None

    class Config:
        orm_mode = True
    