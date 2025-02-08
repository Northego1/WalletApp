from typing import Self
import uuid

from app.exceptions.wallet_exceptions import WalletError
from app.wallet.application.protocols import WalletGetBalanceUseCaseProtocol


class WalletGetBalance:
    def __init__(self: Self, balance_use_case: WalletGetBalanceUseCaseProtocol) -> None:
        self.balance_use_case = balance_use_case


    async def get_balance(self: Self, wallet_id: uuid.UUID):
        try:
            wallet_balance_dto = await self.balance_use_case.get_balance(wallet_id=wallet_id)
        except WalletError as e:
            ...