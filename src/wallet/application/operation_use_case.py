from typing import Self
import uuid
from WalletApp.src.core.wallet_exceptions import WalletNotFoundError
from WalletApp.src.core.uow import UnitOfWork
from wallet.infrastructure.repository.protocols import WalletRepositoryProtocol
from schemas.dto.wallet_dto import WalletBalanceDto


class WalletDepositUseCase:
    def __init__(self: Self, uow: UnitOfWork[WalletRepositoryProtocol]) -> None:
        self.uow = uow

    async def operation(
        self: Self, wallet_id: uuid.UUID, amount: float
    ) -> WalletBalanceDto:
        async with self.uow:
            wallet = await self.uow.repository.get_wallet_for_update(
                wallet_id=wallet_id
            )
            if not wallet:
                raise WalletNotFoundError(
                    status_code=404, detail=f"Wallet {wallet_id!r} not found"
                )
            wallet.deposit(amount=amount)
            await self.uow.repository.update_wallet_balance(
                wallet_id=wallet_id, new_balance=wallet.balance
            )
            return WalletBalanceDto(wallet_id=wallet_id, balance=wallet.balance)


class WalletWithDrawUseCase:
    def __init__(self: Self, uow: UnitOfWork[WalletRepositoryProtocol]) -> None:
        self.uow = uow

    async def operation(
        self: Self, wallet_id: uuid.UUID, amount: float
    ) -> WalletBalanceDto:
        async with self.uow:
            wallet = await self.uow.repository.get_wallet_for_update(
                wallet_id=wallet_id
            )
            if not wallet:
                raise WalletNotFoundError(
                    status_code=404, detail=f"Wallet {wallet_id!r} not found"
                )
            wallet.withdraw(amount=amount)
            await self.uow.repository.update_wallet_balance(
                wallet_id=wallet_id, new_balance=wallet.balance
            )
            return WalletBalanceDto(wallet_id=wallet_id, balance=wallet.balance)
