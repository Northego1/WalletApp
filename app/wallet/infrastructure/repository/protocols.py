from typing import Protocol, Self
import uuid

from wallet.domain.wallet import Wallet


class WalletRepositoryProtocol(Protocol):
    async def update_wallet_balance(
            self: Self,
            wallet_id: uuid.UUID,
            new_balance: float
    ):
        ...

    async def get_wallet_by_id(self: Self, wallet_id: uuid.UUID) -> Wallet:
        ...