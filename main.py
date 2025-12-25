from fastapi import FastAPI
from src.controllers.movie_api import router as movie_router
from src.repositories.database import Base
from src.repositories.engine import engine

app = FastAPI(title="Movie Watchlist Tracker")

app.include_router(movie_router)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
