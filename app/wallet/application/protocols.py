from typing import Protocol, Self


class WalletOperationsUseCaseProtocol(Protocol):
    async def operation(self: Self):
        pass