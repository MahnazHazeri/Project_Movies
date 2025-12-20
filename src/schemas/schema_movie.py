from pydantic import BaseModel,Field
from typing import Optional
from src.models import MovieStatus


class MovieResponse_all(BaseModel):
    ...


class MovieResponse_id(BaseModel):
    ...

class MovieStats(BaseModel):
    ...

class MovieCreate(BaseModel):
    title: str = Field(...,min_length=1,max_length=225)
    status: MovieStatus
    release_year: Optional[int] = Field(None, ge=1900,le=2030)
    genre: Optional[str] = None
    rating: Optional[int] = Field(None,ge=1,le=5)
    notes: Optional[str] = None

    class Config:
        from_attributes = True

class MovieUpdate(BaseModel):
    ...

