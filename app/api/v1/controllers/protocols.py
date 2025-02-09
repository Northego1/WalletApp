from typing import Protocol, Self
import uuid

from schemas.wallet_request_scheme import WalletRequestDto


class WalletOperationControllerProtocol(Protocol):
    async def operation(
            self: Self,
            wallet_id: uuid.UUID,
            wallet_request_dto: WalletRequestDto
    ):
        pass


class WalletGetBalanceControllerProtocol(Protocol):
    async def get_balance(
            self: Self,
            wallet_id: uuid.UUID
    ):
        pass