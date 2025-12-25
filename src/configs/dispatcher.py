from fastapi import FastAPI
from archipy.helpers.utils.base_utils import BaseUtils
from archipy.models.errors import (
    UnauthenticatedError,
    UnknownError,
    UnavailableError,
    InvalidArgumentError,
)

from src.controllers.movie.v1.movie_contollers import routerV1  

def set_dispatch_routes(app: FastAPI) -> None:
    common_private_response = BaseUtils.get_fastapi_exception_responses(
        [
            UnauthenticatedError,
            UnknownError,
            UnavailableError,
            InvalidArgumentError,
        ],
    )

    app.include_router(
        router=routerV1,
        prefix="/api/v1/movies",
        responses=common_private_response,
    )
