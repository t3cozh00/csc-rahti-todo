from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main.core.config import get_app_settings

settings = get_app_settings()

# engine = create_engine(url=settings.database_url, echo=True, future=True)

# Dynamic check: add multi-threading argument if SQLite, keep as-is if Postgres for next week
connect_args = {"check_same_thread": False} if "sqlite" in str(settings.database_url) else {}

engine = create_engine(
    url=settings.database_url, 
    echo=True, 
    future=True,
    connect_args=connect_args
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    """
    Generator dependency yield database connection.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
