from contextlib import asynccontextmanager
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
    AsyncConnection
)

from sqlalchemy.orm import DeclarativeBase
from config import settings


engine = create_async_engine(
    url=settings.db.db_dsn
)

async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=True)


async def get_connection() -> AsyncGenerator[AsyncConnection, None]:
    async with engine.connect() as conn:
        yield conn


class Base(DeclarativeBase):
    pass