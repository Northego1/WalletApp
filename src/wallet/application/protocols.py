from typing import Protocol, Self
import uuid

from schemas.dto.wallet_dto import WalletBalanceDto


class WalletOperationsUseCaseProtocol(Protocol):
    async def operation(
        self: Self, wallet_id: uuid.UUID, amount: float
    ) -> WalletBalanceDto: ...


class WalletGetBalanceUseCaseProtocol(Protocol):
    async def get_wallet_balance(
        self: Self, wallet_id: uuid.UUID
    ) -> WalletBalanceDto: ...
