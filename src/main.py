from fastapi import FastAPI
from src.controllers.movi_router import router as movie_router


app=FastAPI(
    title = "Movie API",
    description = "A simple Movie API using Clean Architecture & ArchiPy patterns",
    version="1.0.0"
)

app.include_router(movie_router)