from decimal import Decimal
from typing import Optional, Type
import uuid

from fastapi import HTTPException
import pytest

from WalletApp.src.wallet.controllers.wallet.operation import WalletOperationController
from container import container
from schemas.dto.wallet_dto import WalletBalanceDto
from schemas.responses.wallet_response_schemes import (
    WalletOperationResponse200,
    WalletBalance,
)
from schemas.requests.wallet_request_schemes import WalletRequestModel, OperationType
from tests.unit.mocks.mock_objects import mock_balance_dto
from tests.unit.mocks.mock_operation_use_case import (
    MockWalletDepositUseCase,
    MockWalletWithdrawUseCase,
)
from dependency_injector import providers


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "wallet_id, request_dto, expection, exception",
    [
        (
            mock_balance_dto.wallet_id,
            WalletRequestModel(operationType=OperationType.DEPOSIT, amount=Decimal(100)),
            WalletOperationResponse200(
                detail=WalletBalance(
                    wallet_id=mock_balance_dto.wallet_id,
                    balance=mock_balance_dto.balance,
                )
            ),
            None,
        ),
        (
            "uncorrect data",
            WalletRequestModel(operationType=OperationType.DEPOSIT, amount=Decimal(100)),
            None,
            HTTPException,
        ),
    ],
)
async def test_wallet_deposit_controller(
    wallet_id: uuid.UUID,
    request_dto: WalletRequestModel,
    expection: Optional[WalletBalanceDto],
    exception: Optional[Type[Exception]],
):
    container.wallet_operation_controller.override(
        providers.Factory(
            WalletOperationController,
            use_case_operation_dict=providers.Dict(
                {OperationType.DEPOSIT: MockWalletDepositUseCase}
            ),
        )
    )
    wallet_operation_controller = container.wallet_operation_controller()

    if exception:
        with pytest.raises(exception):
            assert await wallet_operation_controller.operation(
                wallet_id=wallet_id, wallet_request_dto=request_dto
            )
    else:
        assert (
            await wallet_operation_controller.operation(
                wallet_id=wallet_id, wallet_request_dto=request_dto
            )
            == expection
        )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "wallet_id, request_dto, expection, exception",
    [
        (
            mock_balance_dto.wallet_id,
            WalletRequestModel(operationType=OperationType.WITHDRAW, amount=Decimal(100)),
            WalletOperationResponse200(
                detail=WalletBalance(
                    wallet_id=mock_balance_dto.wallet_id,
                    balance=mock_balance_dto.balance,
                )
            ),
            None,
        ),
        (
            "uncorrect data",
            WalletRequestModel(operationType=OperationType.WITHDRAW, amount=Decimal(100)),
            None,
            HTTPException,
        ),
    ],
)
async def test_wallet_withdraw_controller(
    wallet_id: uuid.UUID,
    request_dto: WalletRequestModel,
    expection: Optional[WalletBalanceDto],
    exception: Optional[Type[Exception]],
):
    container.wallet_operation_controller.override(
        providers.Factory(
            WalletOperationController,
            use_case_operation_dict=providers.Dict(
                {OperationType.WITHDRAW: MockWalletWithdrawUseCase}
            ),
        )
    )
    wallet_operation_controller = container.wallet_operation_controller()

    if exception:
        with pytest.raises(exception):
            assert await wallet_operation_controller.operation(
                wallet_id=wallet_id, wallet_request_dto=request_dto
            )
    else:
        assert (
            await wallet_operation_controller.operation(
                wallet_id=wallet_id, wallet_request_dto=request_dto
            )
            == expection
        )
