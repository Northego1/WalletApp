from typing import Optional, Type
import uuid

import pytest
from fastapi import HTTPException

from container import container
from schemas.dto.wallet_dto import WalletBalanceDto
from schemas.responses.wallet_response_schemes import WalletOperationResponse200, WalletBalance
from schemas.requests.wallet_request_schemes import WalletRequestModel, OperationType
from tests.unit.mocks.mock_objects import mock_balance_dto
from tests.unit.mocks.mock_deposit_use_case import MockWalletDepositUseCase
from dependency_injector import providers
from api.v1.controllers.wallet.operation import WalletOperationController
from wallet.application.operation_use_case import WalletDepositUseCase





@pytest.mark.asyncio
@pytest.mark.parametrize(
    "wallet_id, request_dto, expection, exception",
    [
        (
            mock_balance_dto.wallet_id,
            WalletRequestModel(operationType=OperationType.DEPOSIT, amount=100),
            WalletOperationResponse200(detail=WalletBalance(
                wallet_id=mock_balance_dto.wallet_id,
                balance=mock_balance_dto.balance
            )),
            None
        ),
    ]
)
async def test_wallet_balance_controller(
    wallet_id: uuid.UUID,
    request_dto: WalletRequestModel,
    expection: Optional[WalletBalanceDto],
    exception: Optional[Type[Exception]]
):
    container.wallet_operation_controller.override(
        providers.Factory(
            WalletOperationController,
            use_case_operation_dict=providers.Dict({
                OperationType.DEPOSIT: MockWalletDepositUseCase
            })
        )
    )
    wallet_operation_controller = container.wallet_operation_controller()

    if exception:
        with pytest.raises(exception):
            assert await wallet_operation_controller.operation(
                wallet_id=wallet_id, 
                wallet_request_dto=request_dto
            )
    else:
        assert await wallet_operation_controller.operation(
            wallet_id=wallet_id, 
            wallet_request_dto=request_dto
        ) == expection