from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


SessionLocal = sessionmaker(bind=create_engine(url='sqlite:///taskmanager.db', echo=True))


class Base(DeclarativeBase):
    pass
