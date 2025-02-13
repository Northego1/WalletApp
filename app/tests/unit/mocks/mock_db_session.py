from typing import Self
from common.uow import SessionProtocol


class MockSession(SessionProtocol):
    @classmethod
    async def connect(cls) -> Self:
        return cls()


