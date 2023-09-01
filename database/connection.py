import logging
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from decouple import config


logger = logging.getLogger(__name__)

user = config('DB_USER')
password = config('DB_PASSWORD')
host = config('DB_HOST')
name = config('DB_NAME')


def make_connection_string() -> str:
    url = f"postgresql+asyncpg://{user}:{password}" \
          f"@{host}/{name}" \
          f"?async_fallback=True"
    return url


def create_pool(url: str) -> sessionmaker:
    engine = create_async_engine(url, echo=True)
    return sessionmaker(
        bind=engine,
        expire_on_commit=False,
        class_=AsyncSession,
        future=True,
        autoflush=False,
    )
