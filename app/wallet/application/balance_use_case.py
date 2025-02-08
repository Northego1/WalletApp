from typing import Self
import uuid

from app.schemas.dto.wallet_balance_dto import WalletBalanceDto
from app.wallet.infrastructure.repository.protocols import WalletRepositoryProtocol


class WalletGetBalanceUseCase:
    def __init__(self: Self, wallet_repository: WalletRepositoryProtocol) -> None:
        self.wallet_repository = wallet_repository


    async def get_wallet_balance(self: Self, wallet_id: uuid.UUID) -> WalletBalanceDto:
        wallet = await self.wallet_repository.get_wallet_by_id(wallet_id=wallet_id)
        return WalletBalanceDto(wallet_id=wallet_id, balance=wallet.balance)