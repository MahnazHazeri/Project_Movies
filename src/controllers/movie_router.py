from fastapi import APIRouter,HTTPException, Depends,status
from sqlalchemy.ext.asyncio import AsyncSession
from src.db import get_db
from src.services import MovieOperation
from src.schemas import MovieResponse_all,MovieResponse_id,MovieStats,MovieCreate,MovieUpdate
from src.repositories.movie_repo import MovieRepository
from uuid import UUID



router = APIRouter()
# ----------------------------------------------------------------------------------------
@router.get("/all")
async def all_movie(data: MovieResponse_all):
    ...
# ----------------------------------------------------------------------------------------
@router.get("/{movie_uuid}")
async def id_movie(movie_uuid: UUID, db: AsyncSession=Depends(get_db)):
    repo = MovieRepository(db)
    service = MovieOperation(repo)

    try:
        movie = await service.get_movie_by_id(movie_uuid)
        return movie
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
# ----------------------------------------------------------------------------------------
@router.get("/statistics")
async def statistics_movie(data: MovieStats):
    ...
# ----------------------------------------------------------------------------------------
@router.post("/add")
async def add_movie(data: MovieCreate, db: AsyncSession = Depends(get_db)):
    repo = MovieRepository(db)
    service = MovieOperation(repo)
    return await service.create(**data.model_dump())
# ----------------------------------------------------------------------------------------
@router.put("/updat")
async def update_movie(data: MovieUpdate = Body()):
    ...
# ----------------------------------------------------------------------------------------
@router.delete("/delete")
async def delete_movie():
    ...