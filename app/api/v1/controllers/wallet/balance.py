from typing import Self
import uuid

from schemas.dto.wallet_dto import WalletBalanceDto
from exceptions.wallet_exceptions import WalletError
from wallet.application.protocols import WalletGetBalanceUseCaseProtocol


class WalletGetBalance:
    def __init__(self: Self, balance_use_case: WalletGetBalanceUseCaseProtocol) -> None:
        self.balance_use_case = balance_use_case


    async def get_balance(self: Self, wallet_id: uuid.UUID) -> WalletBalanceDto:
        wallet_balance_dto = await self.balance_use_case.get_wallet_balance(wallet_id=wallet_id)
        return wallet_balance_dto
