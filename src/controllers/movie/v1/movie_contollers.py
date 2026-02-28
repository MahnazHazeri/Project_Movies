from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from uuid import UUID

from dependency_injector.wiring import inject, Provide
from src.configs.container import ServiceContainer
from src.logics.movie.movie_logic import MovieLogic
from src.schemas.movie import MovieCreate, MovieUpdate, MovieResponse, MovieStats

router = APIRouter(prefix="/api/v1/movies", tags=["Movies"])


@router.post("/", response_model=MovieResponse)
@inject
async def create_movie(
    payload: MovieCreate,
    logic: MovieLogic = Depends(Provide[ServiceContainer.movie_logic]),
):
    return await logic.create_movie(payload)


@router.get("/stats", response_model=MovieStats)
@inject
async def get_stats(
    logic: MovieLogic = Depends(Provide[ServiceContainer.movie_logic]),
):
    return await logic.get_stats()


@router.get("/", response_model=List[MovieResponse])
@inject
async def list_movies(
    status: Optional[str] = Query(None),
    genre: Optional[str] = Query(None),
    rating: Optional[int] = Query(None, ge=1, le=5),
    logic: MovieLogic = Depends(Provide[ServiceContainer.movie_logic]),
):
    return await logic.list_movies(status, genre, rating)


@router.get("/{movie_id}", response_model=MovieResponse)
@inject
async def get_movie(
    movie_id: UUID,
    logic: MovieLogic = Depends(Provide[ServiceContainer.movie_logic]),
):
    return await logic.get_movie(movie_id)


@router.put("/{movie_id}", response_model=MovieResponse)
@inject
async def update_movie(
    movie_id: UUID,
    payload: MovieUpdate,
    logic: MovieLogic = Depends(Provide[ServiceContainer.movie_logic]),
):
    return await logic.update_movie(movie_id, payload)


@router.delete("/{movie_id}")
@inject
async def delete_movie(
    movie_id: UUID,
    logic: MovieLogic = Depends(Provide[ServiceContainer.movie_logic]),
):
    await logic.delete_movie(movie_id)
    return {"detail": "Movie deleted successfully"}