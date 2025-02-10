from typing import Self
import uuid

from fastapi import HTTPException

from schemas.responses.wallet_response_schemes import (
    WalletBalance,
    WalletBalanceResponse200,
    WalletOperationResponse200
)
from wallet.application.protocols import WalletOperationsUseCaseProtocol
from schemas.requests.wallet_request_schemes import WalletRequestModel, OperationType
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
            wallet_request_dto: WalletRequestModel
    ) -> WalletOperationResponse200:
        try:
            operation_use_cases = self.use_case_operation_dict[wallet_request_dto.operationType]
            wallet_balance_dto = await operation_use_cases.operation(wallet_id=wallet_id, amount=wallet_request_dto.amount)
            return WalletOperationResponse200(
                detail=WalletBalance(
                    wallet_id=wallet_balance_dto.wallet_id,
                    balance=wallet_balance_dto.balance
                )
            )
        except WalletError as e:
            raise HTTPException(
                status_code=e.status_code,
                detail=e.detail
            )