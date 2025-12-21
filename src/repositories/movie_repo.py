from contextlib import asynccontextmanager
from typing import Any
from archipy.adapters.base.sqlalchemy.adapters import AsyncBaseSQLAlchemyAdapter
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.model import Movie
from sqlalchemy import select, func

class MovieRepository(AsyncBaseSQLAlchemyAdapter[Movie]):


    def __init__(self, session: AsyncSession):
        super().__init__(session)

        self.session = session

    @asynccontextmanager
    async def _create_async_session_manager(self,configs: Any = None):
        yield self.session


    async def  get_stats(self):

        query = select(
            Movie.status,
            func.count(Movie.pk_uuid),
            func.avg(Movie.rating)).group_by(Movie.status)
        
        result = await self.session.execute(query)
        return result.all()




