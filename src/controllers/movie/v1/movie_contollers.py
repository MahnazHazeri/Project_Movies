from fastapi import APIRouter, Depends, Query, Path
from typing import List, Optional

from src.configs.contauners import ServiceContainer
from src.logics.movie.movie_logic import MovieLogic
from src.schemas.movie import MovieCreate, MovieUpdate, MovieResponse, MovieStats

routerV1 = APIRouter(tags=["Movies"])
container = ServiceContainer()

@routerV1.post("/", response_model=MovieResponse, summary="Add a new movie")
async def create_movie(
    payload: MovieCreate,
    logic: MovieLogic = Depends(container.movie_logic),
):
    return await logic.create_movie(payload)

@routerV1.get("/", response_model=List[MovieResponse], summary="Get movies list")
async def list_movies(
    status: Optional[str] = Query(None),
    genre: Optional[str] = Query(None),
    rating: Optional[int] = Query(None, ge=1, le=5),
    logic: MovieLogic = Depends(container.movie_logic),
):
    return await logic.list_movies(status, genre, rating)

@routerV1.get("/{movie_id}", response_model=MovieResponse, summary="Get movie details")
async def get_movie(
    movie_id: str = Path(...),
    logic: MovieLogic = Depends(container.movie_logic),
):
    return await logic.get_movie(movie_id)

@routerV1.put("/{movie_id}", response_model=MovieResponse, summary="Update movie")
async def update_movie(
    movie_id: str,
    payload: MovieUpdate,
    logic: MovieLogic = Depends(container.movie_logic),
):
    return await logic.update_movie(movie_id, payload)

@routerV1.delete("/{movie_id}", summary="Delete movie")
async def delete_movie(
    movie_id: str,
    logic: MovieLogic = Depends(container.movie_logic),
):
    await logic.delete_movie(movie_id)
    return {"detail": "Movie deleted successfully"}

@routerV1.get("/stats", response_model=MovieStats, summary="Movies statistics")
async def get_stats(
    logic: MovieLogic = Depends(container.movie_logic),
):
    return await logic.get_stats()
