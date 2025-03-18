from typing import Self
from WalletApp.src.core.uow import SessionProtocol


class MockSession(SessionProtocol):
    @classmethod
    async def connect(cls) -> Self:
        return cls()
