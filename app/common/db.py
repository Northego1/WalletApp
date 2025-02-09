from contextlib import asynccontextmanager
from typing import AsyncGenerator, Self
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncConnection
)

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import async_scoped_session
from config import settings


class DataBase:
    def __init__(self: Self, url: str) -> None:
        self._engine = create_async_engine(url=url)
        

    @asynccontextmanager
    async def connection(self: Self) -> AsyncGenerator[AsyncConnection, None]:
        async with self._engine.begin() as conn:
            yield conn



engine = create_async_engine(
    url=settings.db.dsn
)



# async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=True)

# async def get_connection() -> AsyncGenerator[AsyncConnection, None]:
#     async with engine.connect() as conn:
#         yield conn


class Base(DeclarativeBase):
    pass