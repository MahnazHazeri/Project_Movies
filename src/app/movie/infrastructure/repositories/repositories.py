from sqlalchemy.orm import Session
from src.app.movie.models.dtos import Movies

class MovieRepository:
    def __init__(self, db:Session):
        self.db = db

    def get_all(self):
        return self.db.query(Movies).all()
    
    def get_by_id(self,  movie_id:int):
        return self.db.query(Movies).filter(Movies.movie_uuid == movie_id).first()
    
    def get_by_title(self, title:str):
        return self.db.query(Movies).filter(Movies.title == title).first()
    
    def creat(self,movie:Movies):
        self.db.add(movie)
        self.db.commit()
        self.db.refresh(movie)
        return movie

