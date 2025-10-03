from sqlalchemy.orm import Session
from src.models.movie_model import Movies



class MovieRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Movies).all()

    def get_by_id(self, movie_uuid:int):
        return self.db.query(Movies).filter(Movies.movie_uuid == movie_uuid).first()


    def get_by_title(self,title:str):
        return  self.db.query(Movies).filter(Movies.title == title).first()

    def creat(self, movie:Movies):
        self.db.add(movie)
        self.db.commit()
        self.db.refresh(movie)
        return movie

    def update(self, movie:Movies, movie_uuid: int = None, title:str = None):
        if movie_uuid:
            db_movie = self.get_by_id(movie_uuid)
        elif title:
            db_movie = self.get_by_title(title)
        else:
            raise ValueError("You must provide either movie_id or title for update!")
        if not db_movie:
            return None
    
        for attr, value in movie.__dict__.items():
            if attr != "_sa_instance_state" and value is not None:
                setattr(db_movie, attr,value)

            self.db.commit()
            self.db.refresh(db_movie)
            return db_movie
    

    def delete(self, movie_uuid: int = None, title:str =None):
        if movie_uuid:
            db_movie = self.get_by_id(movie_uuid)
        elif title:
            db_movie = self.get_by_title(title)
        else:
            raise ValueError("You must provide either movie_id or title for delete!")
        
        if db_movie:
            self.db.delete(db_movie)
            self.db.commit()
            return True
        return False
