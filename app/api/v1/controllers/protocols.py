from typing import Protocol, Self
import uuid

from app.schemas.wallet_request_scheme import WalletRequestDto


class WalletOperationProtocol(Protocol):
    async def operation(
            self: Self,
            wallet_id: uuid.UUID,
            wallet_request_dto: WalletRequestDto
    ):
        pass


class WalletGetBalanceProtocol(Protocol):
    async def get_balance(
            self: Self,
            wallet_id: uuid.UUID
    ):
        pass