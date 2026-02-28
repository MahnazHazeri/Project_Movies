from fastapi import FastAPI
from src.controllers.movie.v1.movie_contollers import router
from src.configs.container import ServiceContainer
from src.repositories.engine import engine
from archipy.models.entities.sqlalchemy.base_entities import BaseEntity

container = ServiceContainer()

app = FastAPI(title="Movie Watchlist Tracker")
app.container = container
app.include_router(router)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(BaseEntity.metadata.create_all)