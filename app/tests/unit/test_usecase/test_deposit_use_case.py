from typing import Optional, Type
import uuid

import pytest
from dependency_injector import providers

from common.uow import UnitOfWork
from container import container
from exceptions.wallet_exceptions import WalletDepositError
from schemas.dto.wallet_dto import WalletBalanceDto
from schemas.requests.wallet_request_schemes import OperationType
from tests.unit.mocks.mock_objects import mock_balance_dto
from wallet.application.operation_use_case import WalletDepositUseCase
from tests.unit.mocks.mock_wallet_repository import MockWalletRepository
from tests.unit.mocks.mock_db_session import MockSession

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "wallet_id, amount, expection, exception",
    [
        (
            mock_balance_dto.wallet_id,
            100,
            WalletBalanceDto(wallet_id=mock_balance_dto.wallet_id, balance=200),
            None
        ),
        (
            mock_balance_dto.wallet_id,
            0,
            None,
            WalletDepositError
        )
    ]
)
async def test_wallet_deposit_use_case(
    wallet_id: uuid.UUID,
    amount: float,
    expection: Optional[WalletBalanceDto],
    exception: Optional[Type[Exception]]
):
    container.operations_use_cases.override(
        providers.Dict({
            OperationType.DEPOSIT: providers.Factory(
                WalletDepositUseCase,
                uow=providers.Factory(
                    UnitOfWork,
                    repository_factory=MockWalletRepository,
                    session_factory=MockSession
                )
            )
        }
        )

    )
    wallet_deposit_use_case = container.operations_use_cases()[OperationType.DEPOSIT]

    if exception:
        with pytest.raises(exception):
            assert await wallet_deposit_use_case.operation(
                wallet_id=wallet_id,
                amount=amount
            )
    else:
        assert await wallet_deposit_use_case.operation(
            wallet_id=wallet_id,
            amount=amount 
        ) == expection







