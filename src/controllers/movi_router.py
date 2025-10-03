from fastapi import APIRouter, Depends,HTTPException,status
from sqlalchemy.orm import Session
from src.services.movie_service import MovieCommandService,MovieQueryService
from src.schemas.movie_schema import MovieCreate,MovieResponse,MovieUpdate
from src.db.dependencies import get_db


router = APIRouter(prefix="/movie",tags =["Movies"])

# -------------------------- Get information about all movies------------------------------
@router.get("/",response_model=list[MovieResponse])
def list_movies(db:Session=Depends(get_db)):
    service = MovieQueryService(db)
    return service.list_movie()

# ---------------------------Get information a special movie by id or title----------------

@router.get("/detail",response_model=MovieResponse)
def get_movie(
    movi_uuid: int | None = None, 
    title:str |None = None,
    db:Session=Depends(get_db)
    ):
    service = MovieQueryService(db)
    try:
        return service.get_movie(movie_uuid=movi_uuid, title = title)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# -----------------------------Enter new information---------------------------------------
   
@router.post("/",response_model=MovieResponse,status_code=status.HTTP_201_CREATED)
def creat_movie(movie: MovieCreate, db:Session=Depends(get_db)):
    service = MovieCommandService(db)
    try:
        return service.add_movie(movie)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

# ----------------------------Edit the desired movie information --------------------------   

@router.put("/",response_model=MovieResponse)
def update_movie(
    movie_uuid:int | None = None,
    title: str|None = None,
    update_data: MovieUpdate = None,
    db:Session=Depends(get_db)   
    ):
    service = MovieCommandService(db)
    try:
        return service.update_movie(movie_uuid=movie_uuid , title = title)
    
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

#------------------------------Delete the desired movie------------------------------------
@router.delete("/",status_code=status.HTTP_204_NO_CONTENT)
def delet_movie(
    movie_uuid:int | None = None,
    title:str | None = None,
    db:Session=Depends(get_db)
    ):
    service = MovieCommandService(db)
    try:

        service.delet_movie(movie_uuid=movie_uuid,title=title)
        return {"detail":"Movie deleted successfully."}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(e))
    

    