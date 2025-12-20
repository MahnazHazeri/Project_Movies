import uuid
from uuid import UUID
from datetime import datetime, timezone
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer,Text,Enum,TIMESTAMP, CheckConstraint
from enum import Enum as PyEnum
from src.db import Base

#------------ Movie status -----------
class MovieStatus(PyEnum):
    watched = "watched"
    want_to_watched = "want_to_watched"


#------------- Movie model ------------
class Movie(Base):
    __tablename__ = "moviedata"

    movie_uuid: Mapped[UUID] = mapped_column(primary_key=True, index=True,default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(225),nullable=False)
    status: Mapped[MovieStatus] = mapped_column(Enum(MovieStatus), nullable=False)
    release_year: Mapped[int | None] = mapped_column(Integer,nullable=True,default=None)
    genre: Mapped[str | None] = mapped_column(String(100),nullable=True,default=None)
    rating: Mapped[int | None] = mapped_column(Integer,nullable=True,default=None)
    notes: Mapped[str | None] = mapped_column(Text ,nullable=True,default=None)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=lambda:datetime.now(timezone.utc))

    # Validation for rating and release_year
    __table_args__ = (
        CheckConstraint('(rating BETWEEN 1 AND 5) OR rating IS NULL', name='rating_check'),
        CheckConstraint('(release_year BETWEEN 1900 AND 2030) OR release_year IS NULL', name='release_year_check')
    )
