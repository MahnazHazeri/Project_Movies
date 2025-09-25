from fastapi import FastAPI
from routers import Movies

app = FastAPI()
app.include_router(Movies.router, tags=['Movies'])
