from typing import Self
import uuid

from wallet.application.protocols import WalletOperationsUseCaseProtocol
from app.schemas.wallet_request_scheme import WalletRequestDto, OperationType
from exceptions.wallet_exceptions import WalletError


class WalletOperationController:
    def __init__(
            self: Self,
            operations: dict[OperationType, WalletOperationsUseCaseProtocol]
    ) -> None:
        self.operations = operations


    async def operation(
            self: Self,
            user_id: uuid.UUID,
            wallet_request_dto: WalletRequestDto
    ):
        try:
            operation = self.operations[wallet_request_dto.operationType]

        except WalletError as e:
            