from decimal import Decimal
from typing import Optional, Protocol, Self
import uuid

from wallet.domain.wallet import Wallet


class WalletRepositoryProtocol(Protocol):
    async def update_wallet_balance(
        self: Self, wallet_id: uuid.UUID, new_balance: Decimal
    ): ...

    async def get_wallet_for_update(
        self: Self, wallet_id: uuid.UUID
    ) -> Optional[Wallet]: ...

    async def get_wallet_by_id(
        self: Self, wallet_id: uuid.UUID
    ) -> Optional[Wallet]: ...
