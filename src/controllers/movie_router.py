from fastapi import APIRouter,HTTPException, Depends,status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from src.db import get_db
from src.services import MovieOperation
from src.schemas import MovieResponse,MovieStats,MovieCreate,MovieUpdate
from src.repositories.movie_repo import MovieRepository
from uuid import UUID



router = APIRouter()

async def get_movie_service(db_session: AsyncSession = Depends(get_db)) -> MovieOperation:
    repo = MovieRepository(db_session)
    return MovieOperation(repo)

MovieService = Annotated[MovieOperation, Depends(get_movie_service)]



@router.get("/summary/stats")
async def statistics_movie(service: MovieService):
    return await service.get_movie_stats()

# --------------------------------For Get_all--------------------------------------------------------

@router.get("/", response_model=list[MovieResponse])
async def all_movie(service : MovieService):
    return await service.get_all_movies()

# ---------------------------------For Get_id-------------------------------------------------------

@router.get("/{movie_uuid}", response_model=MovieResponse)
async def id_movie(movie_uuid: UUID,service: MovieService):

    try:
        movie = await service.get_movie_by_id(movie_uuid)
        return movie
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    
# ---------------------------------For add_movie-------------------------------------------------------

@router.post("/", status_code = status.HTTP_201_CREATED, response_model=MovieResponse)
async def add_movie(data: MovieCreate,service: MovieService):
    
    try:
        new_movie =await service.create(**data.model_dump())
        return new_movie
    except Exception as e:
        print(f"DEBUG:{str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=str(e)
            )
    
# ----------------------------For Update------------------------------------------------------------

@router.put("/{movie_uuid}",response_model=MovieResponse)
async def update_movie(
    movie_uuid:UUID,
    data: MovieUpdate,
    service: MovieService
    ):


    try:
        update_data = data.model_dump(exclude_unset=True)
        return await service.update_movie(movie_uuid, update_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))



# -----------------------------For delete-------------------------------------------------------------------

@router.delete("/{movie_uuid}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_movie(movie_uuid: UUID, service: MovieService):
    try:
        await service.delete_movie(movie_uuid)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The requested movie was not found!")

# ----------------------------------------------------------------------------------------
    