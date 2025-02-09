from typing import Self
import uuid

from wallet.application.protocols import WalletOperationsUseCaseProtocol
from schemas.wallet_request_scheme import WalletRequestDto, OperationType
from exceptions.wallet_exceptions import WalletError


class WalletOperationController:
    def __init__(
            self: Self,
            use_case_operation_dict: dict[OperationType, WalletOperationsUseCaseProtocol]
    ) -> None:
        self.use_case_operation_dict = use_case_operation_dict


    async def operation(
            self: Self,
            wallet_id: uuid.UUID,
            wallet_request_dto: WalletRequestDto
    ):
        try:
            operation_use_cases = self.use_case_operation_dict[wallet_request_dto.operationType]
            await operation_use_cases.operation(wallet_id=wallet_id, amount=wallet_request_dto.amount)
            
        except WalletError as e:
            ...