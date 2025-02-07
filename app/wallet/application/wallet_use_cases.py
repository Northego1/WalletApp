from typing import Protocol, Self


class WalletDepositUseCase(Protocol):
    async def operation(self: Self):
        pass


class WalletWithDrawUseCase(Protocol):
    async def operation(self: Self):
        pass