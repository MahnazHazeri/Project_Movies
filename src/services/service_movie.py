from src.repositories.movie_repo import MovieRepository
from src.models import Movie,MovieStatus
from uuid import UUID


class MovieOperation:
    def __init__(self, repository: MovieRepository) -> None:
        self.repository = repository

# -----------------For add_movie--------------

    async def create(self, **data) -> Movie:
        movie = await self.repository.create(data)
        await self.repository.session.commit()
        await self.repository.session.refresh(movie)
        return movie

        
# -----------------For get_movie_id------------  

    async def get_movie_by_id(self, movie_uuid:UUID) -> Movie:
        movie = await self.repository.get_by_id(movie_uuid)
        if not movie:
            raise ValueError(f"Movie with id{movie_uuid} not found!")
        return movie
    
# -----------------For get_all_movie--------------

    async def get_all_movies(self):
        return await self.repository.get_all()
    
# -----------------For update---------------------------------------

    async def update_movie(self, movie_uuid: UUID, data: dict) -> Movie:
        movie = await self.repository.get_by_id(movie_uuid)
        if not movie:
            raise ValueError("No movie with these specifications was found!")
        
        updated_movie = await self.repository.update(movie, data)
        await self.repository.session.commit()
        await self.repository.session.refresh(updated_movie)
        return updated_movie
    
# ----------------------For delete ----------------------------------------

    async def delete_movie(self, movie_uuid: UUID) -> None:
        movie = await self.get_movie_by_id(movie_uuid)

        await self.repository.delete(movie)
        await self.repository.session.commit()

# ----------------------------For statistics --------------------------------
    async def get_movie_stats(self):
        raw_stats = await self.repository.get_stats()
        stats_dict = {
            "watched": 0,
            "want_to_watched": 0,
            "total_movies": 0,
            "average_rating": 0.0
        }
        total_rating_sum = 0

        for row in raw_stats: 
            status, count, avg_rating = row
            if status.value == "watched":
                stats_dict["watched"] = count
            elif status.value == "want_to_watched":
                stats_dict["want_to_watched"] = count
                
            stats_dict["total_movies"] += count
            if avg_rating:
                total_rating_sum += (avg_rating * count)
        if stats_dict["total_movies"] > 0:
            stats_dict["average_rating"] = round(total_rating_sum / stats_dict["total_movies"],2)
        return stats_dict
