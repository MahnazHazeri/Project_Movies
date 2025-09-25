from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base =declarative_base()


DATABSE_URL = "mysql+pymysql://root:4021362415@localhost:3306/project_movie?charset=utf8"
engin = create_engine(DATABSE_URL)
Sessionlocal = sessionmaker( bind = engin, autocommit=False, autoflush=False )
