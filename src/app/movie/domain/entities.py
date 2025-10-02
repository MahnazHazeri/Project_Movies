from dataclasses import dataclass
from typing import Optional


@dataclass
class Movie:
    movie_uuid: Optional[int]=None
    title: str
    genre: str
    release_year: int
    status: str
    notes: Optional[str] = None
    

    
    