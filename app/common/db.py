from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
    AsyncSession
)

from sqlalchemy.orm import DeclarativeBase
from config import settings


engine = create_async_engine(
    url=settings.db.db_dsn
)

async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=True)



async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


class Base(DeclarativeBase):
    pass