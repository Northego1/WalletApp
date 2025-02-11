from typing import Self
import uuid

from exceptions.wallet_exceptions import WalletNotFoundError
from common.uow import UnitOfWork
from schemas.dto.wallet_dto import WalletBalanceDto
from wallet.infrastructure.repository.protocols import WalletRepositoryProtocol


class WalletGetBalanceUseCase:
    def __init__(self: Self, uow: UnitOfWork[WalletRepositoryProtocol]) -> None:
        self.uow = uow


    async def get_wallet_balance(self: Self, wallet_id: uuid.UUID) -> WalletBalanceDto:
        async with self.uow:
            wallet = await self.uow.repository.get_wallet_by_id(wallet_id=wallet_id)
            if not wallet:
                raise WalletNotFoundError(
                        status_code=404,
                        detail=f'Wallet {wallet_id!r} not found'
                    )
            return WalletBalanceDto(
                wallet_id=wallet_id,
                balance=wallet.balance
            )