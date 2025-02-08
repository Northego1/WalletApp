from typing import Protocol, Self
import uuid

from app.schemas.dto.wallet_balance_dto import WalletBalanceDto


class WalletOperationsUseCaseProtocol(Protocol):
    async def operation(self: Self, wallet_id: uuid.UUID, amount: float):
        ...


class WalletGetBalanceUseCaseProtocol(Protocol):
    async def get_balance(self: Self, wallet_id: uuid.UUID) -> WalletBalanceDto:
        ...