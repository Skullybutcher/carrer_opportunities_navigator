from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = scoped_session(SessionLocal)
Base = declarative_base()

def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()
