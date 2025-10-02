from fastapi import APIRouter, Depends, HTTPException,status,Query
from sqlalchemy.orm import Session
from typing import List,Optional

from src.app.movie.application.services.movie_command_service import MovieCommandService
from src.app.movie.application.services.movie_query_service import MovieQueryService
from src.app.movie.infrastructure.database import get_db
from src.app.movie.schemas.movie_schema import MovieCreate,Movieupdate,MovieResponse,MovieStates


router =APIRouter(prefix="/movies",tags=["MOvies"])

# ----------------------Dependecy-------------------------------

def get_movie_command_services(db: Session = Depends(get_db)):
    return MovieCommandService(db)

def get_movie_query_services(db: Session = Depends(get_db)):
    return MovieQueryService(db)

# -------------------------- Get information about all movies----------------------------------------------
@router.get("/",response_model=List[MovieResponse])
def list_movies(service: MovieQueryService = Depends(get_movie_query_services)):
    return service.list_movies

# ---------------------------Get information a special movie by id or title----------------------------------------------
@router.get("/serche", response_model=MovieResponse)
def get_movie(
    movie_id: Optional[int] = None,
    title: Optional[str] = None,
    service: MovieQueryService = Depends(get_movie_query_services)):
    try:
        return service.get_movie(movie_id=movie_id, title=title)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))
    

# -----------------------------Enter new information------------------------------------------------
@router.post("/",response_model=MovieResponse)
def add_movie(movie_data: MovieCreate, service:MovieCommandService=Depends(get_movie_command_services)):
    try:
        return service.add_movie(movie_data.dict())
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
# ----------------------------Edit the desired movie information ------------------------------------
@router.put("/",response_model=MovieResponse)
def update_movie(
            update_data: Movieupdate, 
            movie_id: Optional[int] = None, 
            title: Optional[str] = None,
            service: MovieCommandService = Depends(get_movie_command_services)
            ):
    try:
        return service.update_movie(update_data.dict(exclude_unset=True),movie_id=movie_id,title=title)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))
    
#------------------------------Delete the desired movie-----------------------------------------
@router.delete("/",response_model=dict)
def delete_movie(
    movie_id: Optional[int]=None,
    title: Optional[str]=None,
    service: MovieCommandService = Depends(get_movie_command_services)
    ):
    try:
        service.delete_movie(movie_id=movie_id, title=title)
        return {"detail":"Movie deleted Successfully"}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))
                
# -------------------------Calculating statistics of desired information for movies----------------
@router.get("/stats")
def movie_stats(
    field: Optional[str] =  Query(None,description="total_movies, watched_movies, want_to_watch_movies, average_rating"),
    service: MovieQueryService =Depends(get_movie_query_services)
):
    movies = service.list_movies()

    total_movies = len(movies)
    watched_movies = 0
    want_to_watche_movies = 0
    ratings = []
    for movie in movies:
        if movie.status == "watched" :
            watched_movies += 1
        elif movie.status == "want_to_watche":
            want_to_watche_movies += 1

        if movie.rating is not None:
            ratings.append(movie.rating)

        average_rating = sum(ratings)/len(ratings) if ratings else None

        stats ={
            "total_movies": total_movies,
            "watched_movies": watched_movies,
            "want_to_watche_movies": want_to_watche_movies,
            "average_rating": average_rating
        }
        if field:
            if field not in stats:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid filed name!")
            return {field: stats[field]}
        return stats
    


