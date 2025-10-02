# add,delete,update
from sqlalchemy.orm import Session
from src.app.movie.infrastructure.repositories.repositories import MovieRepository
from src.app.movie.models.dtos import Movies


class MovieCommandService:
    def __init__(self,db:Session):
        self.repo = MovieRepository(db)

# ------------------------add movie-----------------------------------------------------
    def add_movie(self,movie_data:dict):
        existing_movie = self.repo.get_by_title(movie_data["title"])
        if existing_movie:
            raise ValueError("movie alredy existing!")
        movie = Movies(**movie_data) 
        return self.repo.creat(movie)
# -----------------------update movie----------------------------------------------------
    def  update_movie(
            self,
            update_data: dict, 
            movie_id :int = None, 
            title:str = None
        ):

        if  movie_id:
            movie = self.repo.get_by_id(movie_id)
        elif title:
            movie = self.repo.get_by_title(title)
        else:
            raise ValueError("You must enter either the id or the movie title!")
        
        if not movie:
            raise ValueError("The desired movie was not found!")
        if "rating" in  update_data and movie.status != "watched" :
            raise ValueError("You can only rate a movie after watching it!")
        
        for key, value in update_data.items():
            setattr(movie,key,value)
        return self.repo.update(movie)
# -----------------------delete movie-------------------------------------------------------

    def delete_movie(self,movie_id:int = None , title:str=None):
        if movie_id:
            movie = self.repo.get_by_id(movie_id)
        elif title:
            movie = self.repo.get_by_title(title)
        else:
            raise ValueError("You must enter either the id or the movie title!")
    
        if not movie:
            raise ValueError("The desired movie was not found!")
    
        return self.repo.delete(movie.id)
                      
    
        
