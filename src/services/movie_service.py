from sqlalchemy.orm import Session
from src.repositories.movie_repository import MovieRepository
from src.models.movie_model import Movies
from src.schemas.movie_schema import MovieCreate,MovieUpdate

# ---------------------- Command Service ----------------------
class MovieCommandService:
    def __init__(self, db:Session):
        self.repo =MovieRepository(db)

# ----------------------Create a new  movie --------------------
    def add_movie(self, movie_data:MovieCreate):
        existing = self.repo.get_by_title(movie_data.title)
        if existing:
            raise ValueError("Movie already exists!")
        movie = Movies(**movie_data.dict())
        return self.repo.create(movie)
    
# ----------------------- update movie ---------------------------------------------------------------------------------
    def update_movie(self, update_data: MovieUpdate, movie_uuid:int = None, title:str = None):
        if update_data.rating is not None:
            if movie_uuid is not None:
                db_movie = self.repo.get_by_id(movie_uuid)
            elif title is not None:
                db_movie =self.repo.get_by_title(title)
            else:
                db_movie = None
            if db_movie and db_movie.status != "watched":
                raise ValueError("You can only rate a movie after watching it!")
        return self.repo.update(update_data.dict(exclude_unset= True),movie_uuid = movie_uuid, title=title)
    
# ----------------------- delete movie ---------------------------------------------------------------------------------
    def delete_movie(self, movie_uuid: int =None , title:str = None):
        delete = self.repo.delete(movie_uuid = movie_uuid, title=title)
        if not delete:
            raise ValueError("Movie not found!")
        return delete
    
 # ---------------------- **Query Service**-------------------------------------------------------------------------------
class MovieQueryService:
    def __init__(self, db:Session):
        self.repo = MovieRepository(db)
# ---------------------list of all movies --------------------
    def list_movie(self):
        return self.repo.get_all()
# ----------------------- Get movie by id or title ------------
    def get_movie(self,movie_uuid:int = None,title:str=None):
        if movie_uuid is not None:
            movie = self.repo.get_by_id(movie_uuid)
        elif title is not None:
            movie = self.repo.get_by_title(title)
        else:
            movie = None
        if not movie:
            raise ValueError("Movie not found!")
        return movie
    


    
