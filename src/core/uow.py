from typing import Any, Callable, Generic, Protocol, Self, Type, TypeVar
from WalletApp.src.core.wallet_exceptions import WalletError
from sqlalchemy.ext.asyncio import AsyncEngine
import uuid


T = TypeVar("T")


class SessionProtocol(Protocol):
    @classmethod
    async def connect(cls) -> Self: ...
    async def commit(self: Self): ...
    async def rollback(self: Self): ...
    async def close(self: Self): ...


class UnitOfWork(Generic[T]):
    def __init__(
        self: Self,
        repository_factory: Callable[[SessionProtocol], T],
        session_factory: Type[SessionProtocol],
    ) -> None:
        self._repository_factory = repository_factory
        self._session_factory = session_factory

        self._session: SessionProtocol
        self._repository: T

    @property
    def repository(self: Self) -> T:
        if not hasattr(self, "_repository"):
            raise RuntimeError(
                "Use into context manager, and define repository factory"
            )
        return self._repository

    async def __aenter__(self: Self) -> "UnitOfWork":
        self._session = await self._session_factory.connect()
        self._repository = self._repository_factory(self._session)
        return self

    async def __aexit__(self: Self, exc_type: Any, exc: Any, tb: Any):
        if exc_type:
            await self._session.rollback()
            await self._session.close()
            raise WalletError(status_code=400)
        else:
            await self._session.commit()
            await self._session.close()

    async def commit(self: Self):
        if not hasattr(self, "_session"):
            raise RuntimeError("Use into context manager, and define session factory")
        await self._session.commit()

    async def rollback(self: Self):
        if not hasattr(self, "_session"):
            raise RuntimeError("Use into context manager, and define session factory")
        await self._session.rollback()
