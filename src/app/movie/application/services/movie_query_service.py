# get
from  sqlalchemy.orm import Session
from src.app.movie.infrastructure.repositories.repositories import MovieRepository

class MovieQueryService:
    def __init__(self, db:Session):
        self.repo = MovieRepository(db)


# ---------------------------------Getting all the movies-----------------------------------
    def list_movies(self):
        return self.repo.get_all()
    
# ---------------------------------Get video by id or title (optional)-----------------------
    def get_movie(self,
                movie_id:int = None,
                title:str =None
                ):
        if movie_id:
            movie = self.repo.get_by_id(movie_id)
        elif title:
            movie =  self.repo.get_by_title(title)
        else:
            raise ValueError("You must enter either the id or title of the movie!")
        
        if not movie:
            raise ValueError("The desired movie was not found!")
        return movie
    