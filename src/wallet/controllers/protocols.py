from typing import Protocol, Self
import uuid

from schemas.responses.wallet_response_schemes import (
    WalletBalanceResponse200,
    WalletOperationResponse200,
)
from schemas.dto.wallet_dto import WalletBalanceDto
from schemas.requests.wallet_request_schemes import WalletRequestModel


class WalletOperationControllerProtocol(Protocol):
    async def operation(
        self: Self, wallet_id: uuid.UUID, wallet_request_dto: WalletRequestModel
    ) -> WalletOperationResponse200: ...


class WalletGetBalanceControllerProtocol(Protocol):
    async def get_balance(
        self: Self, wallet_id: uuid.UUID
    ) -> WalletBalanceResponse200: ...
