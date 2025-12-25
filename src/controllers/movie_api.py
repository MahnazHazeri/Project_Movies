from fastapi import APIRouter
from src.controllers.movie.v1.movie_contollers import routerV1

router = APIRouter()
router.include_router(routerV1, prefix="/movies")
