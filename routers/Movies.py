from fastapi import  Depends,status,HTTPException,APIRouter
from sqlalchemy.orm import Session
import pydantic_model 
import models
from dependencies import get_db


router = APIRouter()


@router.post('/movie/',response_model=pydantic_model.MovieCreate, status_code=status.HTTP_201_CREATED)
def create_movie(movie:pydantic_model.MovieCreate, db: Session = Depends(get_db)):
# کوئری برای بررسی وجود فیلم که آیا از قبل ذخیره شده یا نه
    existing_movie = db.query(models.Movies).filter(
        models.Movies.title == movie.title,
        models.Movies.genre == movie.genre
        ).first()
    
    if existing_movie:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail="A movie with that title and genre already exists!"
        )
    

    new_movie = models.Movies(
        title = movie.title,
        genre = movie.genre,
        release_year = movie.release_year,
        status_ = movie.status_,
        notes = movie.notes
    )

    
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie
    

# خروجی: اطلاعات کل فیلم های ذخیره شده در دیتابیس
@router.get('/movie/',response_model=pydantic_model.MovieResponse)
def read_allmovies(db:Session = Depends(get_db)):
    pass








# خروجی :اطلاعات فیلم مورد نظر کاربر براساس ایدی فیلم
@router.get('movie/{movie_id}',response_model=pydantic_model.MovieResponse)
def read_movie(movie_id:int, db:Session = Depends(get_db)):
# کوئری برای اینکه فیلمی با ایدی که کاربر ارسال کرده وجود داره یا نه

    exist_movie = db.query(models.Movies).filter(models.Movies.movie_uuid == movie_id).first()
    if exist_movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='movie not found!')
    return exist_movie