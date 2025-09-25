from sqlalchemy import Column, Integer, String ,SmallInteger, Text, DateTime
from databese import Base 
from sqlalchemy.sql import func 
import enum
from sqlalchemy import Enum as SQLEnum




class statusEnum(str,enum.Enum):
    Watched = 'watched'
    want_to_watche = 'want_to_watch'


class Movies(Base):
    __tablename__ = "movies"

    movie_uuid = Column(Integer, primary_key = True)
    title = Column(String(225), unique = True , nullable = False)
    genre = Column(String(225), unique=True , nullable = True)
    release_year =Column(Integer, nullable = True)
    status_ = Column(SQLEnum(statusEnum, name = 'status_enum'),nullable = False)
    rating = Column(SmallInteger, nullable = True)
    notes = Column(Text , nullable = True)
    created_at = Column(DateTime, default = func.now())


 




    