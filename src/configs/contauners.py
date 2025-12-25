from dependency_injector import containers, providers
from archipy.adapters.postgres.sqlalchemy.adapters import AsyncPostgresSQLAlchemyAdapter

from src.configs.runtime_config import RuntimeConfig
from src.logics.movie.movie_logic import MovieLogic
from src.repositories.movie_repository import MovieRepository
from src.repositories.adapters import MoviePostgresAdapter

class ServiceContainer(containers.DeclarativeContainer):
    _config: RuntimeConfig = RuntimeConfig.global_config()

 
    _postgres_adapter = providers.ThreadSafeSingleton(
        AsyncPostgresSQLAlchemyAdapter,
        database_url=_config.database_url,
    )

    _movie_postgres_adapter = providers.ThreadSafeSingleton(
        MoviePostgresAdapter,
        adapter=_postgres_adapter,
    )

    _movie_repository = providers.ThreadSafeSingleton(
        MovieRepository,
        postgres_adapter=_movie_postgres_adapter,
    )

    movie_logic = providers.Factory(
        MovieLogic,
        db=_postgres_adapter.provided.session,
    )
