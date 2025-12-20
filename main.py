from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db import Base, engine
from src.controllers.movie_router  import  router as movie_router





@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)

app.include_router(movie_router,prefix="/movies")


