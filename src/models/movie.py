import uuid
from datetime import datetime
from sqlalchemy import VARCHAR, INTEGER, DateTime, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column,synonym
from archipy.models.entities.sqlalchemy.base_entities import BaseEntity

from src.models.types_ import MovieStatusType


class Movie(BaseEntity):
    __tablename__ = "movies"

    movie_uuid: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )
    pk_uuid = synonym("movie_uuid")
    title: Mapped[str] = mapped_column(VARCHAR(255), nullable=False, index=True)
    genre: Mapped[str | None] = mapped_column(VARCHAR(100), nullable=True)
    release_year: Mapped[int | None] = mapped_column(INTEGER)
    status: Mapped[MovieStatusType] = mapped_column(
        SAEnum(MovieStatusType,name="movie_status_enum",),
        nullable=False,
        default=MovieStatusType.WANT_TO_WATCH,
    )
    rating: Mapped[int | None] = mapped_column(INTEGER)
    notes: Mapped[str | None] = mapped_column(VARCHAR(500))
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )