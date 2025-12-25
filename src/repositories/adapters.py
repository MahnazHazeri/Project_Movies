from archipy.adapters.postgres.sqlalchemy.adapters import AsyncPostgresSQLAlchemyAdapter

class MoviePostgresAdapter:
    def __init__(self, adapter: AsyncPostgresSQLAlchemyAdapter):
        self._adapter = adapter

    @property
    def session(self):
        return self._adapter.session

   
