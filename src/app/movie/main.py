from fastapi import FastAPI
from src.app.movie.interface.api.movie_router import router as movie_router

app = FastAPI(title="Movie API")

app.include_router(movie_router)