from sqlalchemy import create_engine
from sqlalchemmy.declarative.base import declarative_base
from sqlalchemy.orm import sessionmaer

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQL_ALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()