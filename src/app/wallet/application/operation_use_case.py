from typing import Self
import uuid
from wallet.infrastructure.repository.protocols import WalletRepositoryProtocol
from schemas.dto.wallet_dto import WalletBalanceDto


class WalletDepositUseCase:
    def __init__(self: Self, wallet_repository: WalletRepositoryProtocol) -> None:
        self.wallet_repository = wallet_repository
        

    async def operation(self: Self, wallet_id: uuid.UUID, amount: float) -> WalletBalanceDto:
        wallet = await self.wallet_repository.get_wallet_by_id(wallet_id=wallet_id)
        wallet.deposit(amount=amount)
        await self.wallet_repository.update_wallet_balance(
            wallet_id=wallet.id,
            new_balance=wallet.balance
        )
        return WalletBalanceDto(
            wallet_id=wallet_id,
            balance=wallet.balance
        )


class WalletWithDrawUseCase:
    def __init__(self: Self, wallet_repository: WalletRepositoryProtocol) -> None:
        self.wallet_repository = wallet_repository


    async def operation(self: Self, wallet_id: uuid.UUID, amount: float) -> WalletBalanceDto:
        wallet = await self.wallet_repository.get_wallet_by_id(wallet_id=wallet_id)
        wallet.withdraw(amount=amount)
        await self.wallet_repository.update_wallet_balance(
            wallet_id=wallet.id,
            new_balance=wallet.balance
        )
        return WalletBalanceDto(
            wallet_id=wallet_id,
            balance=wallet.balance
        )