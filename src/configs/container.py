from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.engine import AsyncSessionFactory
from src.repositories.adapters import MovieRepository
from src.logics.movie.movie_logic import MovieLogic


class ServiceContainer(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=["src.controllers.movie.v1.movie_contollers"]
    )

    session: providers.Provider[AsyncSession] = providers.Factory(
        AsyncSessionFactory
    )

    movie_repository = providers.Factory(
        MovieRepository,
        session=session,
    )

    movie_logic = providers.Factory(
        MovieLogic,
        movie_repository=movie_repository,
    )