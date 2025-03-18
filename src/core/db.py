from contextlib import asynccontextmanager
from typing import AsyncGenerator, Self
from sqlalchemy.ext.asyncio import create_async_engine, AsyncConnection

from sqlalchemy.orm import DeclarativeBase
from WalletApp.src.core.config import settings


class DataBase:
    def __init__(self: Self, url: str) -> None:
        self.engine = create_async_engine(
            url=url,
            pool_size=settings.db.conn_pool,
            max_overflow=settings.db.conn_max_overflow,
            pool_timeout=settings.db.conn_timeout,
            pool_recycle=settings.db.conn_recycle,
        )

    async def get_ready_connection_pool(self: Self):
        for _ in range(1):
            connect = await self.engine.connect()
            await connect.close()

    @asynccontextmanager
    async def connection(self: Self) -> AsyncGenerator[AsyncConnection, None]:
        async with self.engine.begin() as conn:
            yield conn


class Base(DeclarativeBase):
    pass
