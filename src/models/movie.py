import uuid
from datetime import datetime
from archipy.models.entities.sqlalchemy.base_entities import (UpdatableDeletableEntity)
from sqlalchemy import UUID, VARCHAR, INTEGER, DateTime
from sqlalchemy.orm import Mapped, Synonym, mapped_column
from sqlalchemy import Enum as SAEnum

from src.models.types_ import MovieStatusType



class Movie(UpdatableDeletableEntity):
    __tablename__ = "movies"


    movie_uuid = mapped_column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4,)
    pk_uuid = Synonym("movie_uuid")

    title: Mapped[str] = mapped_column(VARCHAR(255),nullable=False,index=True,)
    genre: Mapped[str | None] = mapped_column(VARCHAR(100),nullable=True,index=True,)
    release_year: Mapped[int | None] = mapped_column(INTEGER, nullable=True,index=True,)
    status: Mapped[MovieStatusType] = mapped_column(SAEnum(MovieStatusType, name="movie_status_enum"),nullable=False,index=True,default=MovieStatusType.WANT_TO_WATCH,)
    rating: Mapped[int | None] = mapped_column(INTEGER,nullable=True,index=True,)
    notes: Mapped[str | None] = mapped_column(VARCHAR(500),nullable=True,)
    created_at: Mapped[datetime] = mapped_column(DateTime(),default=datetime.utcnow,nullable=False,)
