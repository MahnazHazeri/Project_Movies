from fastapi import FastAPI
from src.controllers.movie_api import router as movie_router
from archipy.models.entities.sqlalchemy.base_entities import BaseEntity
from src.repositories.engine import engine

app = FastAPI(title="Movie Watchlist Tracker")

app.include_router(movie_router)

@app.on_event("startup")
async def on_startup():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(BaseEntity.metadata.create_all)
    except Exception as e:
        print("Database startup failed:", e)
