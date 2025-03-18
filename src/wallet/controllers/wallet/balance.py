from typing import Self
import uuid

from fastapi.exceptions import HTTPException

from schemas.dto.wallet_dto import WalletBalanceDto
from WalletApp.src.core.wallet_exceptions import WalletError
from wallet.application.protocols import WalletGetBalanceUseCaseProtocol
from schemas.responses.wallet_response_schemes import (
    WalletBalanceResponse200,
    WalletBalance,
)


class WalletGetBalance:
    def __init__(self: Self, balance_use_case: WalletGetBalanceUseCaseProtocol) -> None:
        self.balance_use_case = balance_use_case

    async def get_balance(self: Self, wallet_id: uuid.UUID) -> WalletBalanceResponse200:
        try:
            wallet_balance_dto = await self.balance_use_case.get_wallet_balance(
                wallet_id=wallet_id
            )
            return WalletBalanceResponse200(
                detail=WalletBalance(
                    wallet_id=wallet_balance_dto.wallet_id,
                    balance=wallet_balance_dto.balance,
                )
            )
        except WalletError as e:
            raise HTTPException(status_code=e.status_code, detail=e.detail)
