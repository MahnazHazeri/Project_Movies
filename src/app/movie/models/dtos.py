from archipy.models.entities.sqlalchemy.base_entities import BaseEntity
from sqlalchemy import Column,Integer,String,SmallInteger,Text,DateTime,UniqueConstraint
from sqlalchemy.sql import func
import enum
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import synonym 


class StatuseEnum(str,enum.Enum):
    Watched ='watched'
    Want_to_watche ='want_to_watch'



class Movies(BaseEntity):
    __tablename__ = "movies"

    movie_uuid = Column(Integer, primary_key=True)
    pk_uuid = synonym('movie_uuid')
    title = Column(String(225),nullable=False)
    genre = Column(String(225),nullable=True)
    release_year = Column(Integer,nullable=True)
    status = Column(
        SQLEnum(StatuseEnum, name="status_enum"),
        nullable=False
    )
    rating = Column(SmallInteger,nullable=True)
    notes = Column(Text,nullable=True)
    created_at = Column(DateTime,default=func.now())

    __table_args__ = (
        UniqueConstraint("title","release_year",name="uq_title_year"),
    )
    


