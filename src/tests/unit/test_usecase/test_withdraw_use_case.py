from decimal import Decimal
from typing import Optional, Type
import uuid

import pytest
from dependency_injector import providers

from WalletApp.src.core.uow import UnitOfWork
from WalletApp.src.wallet.domain.wallet import WalletWithDrawError
from container import container
from schemas.dto.wallet_dto import WalletBalanceDto
from schemas.requests.wallet_request_schemes import OperationType
from tests.unit.mocks.mock_objects import mock_balance_dto
from wallet.application.operation_use_case import WalletWithDrawUseCase
from tests.unit.mocks.mock_wallet_repository import MockWalletRepository
from tests.unit.mocks.mock_db_session import MockSession


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "wallet_id, amount, expection, exception",
    [
        (
            mock_balance_dto.wallet_id,
            100,
            WalletBalanceDto(wallet_id=mock_balance_dto.wallet_id, balance=Decimal(0)),
            None,
        ),
        (
            mock_balance_dto.wallet_id,
            100,
            WalletBalanceDto(wallet_id=mock_balance_dto.wallet_id, balance=Decimal(0)),
            None,
        ),
        (mock_balance_dto.wallet_id, Decimal(200), None, WalletWithDrawError),
    ],
)
async def test_wallet_withdraw_use_case(
    wallet_id: uuid.UUID,
    amount: float,
    expection: Optional[WalletBalanceDto],
    exception: Optional[Type[Exception]],
):
    container.operations_use_cases.override(
        providers.Dict(
            {
                OperationType.WITHDRAW: providers.Factory(
                    WalletWithDrawUseCase,
                    uow=providers.Factory(
                        UnitOfWork,
                        repository_factory=MockWalletRepository,
                        session_factory=MockSession,
                    ),
                )
            }
        )
    )
    wallet_withdraw_use_case = container.operations_use_cases()[OperationType.WITHDRAW]

    if exception:
        with pytest.raises(exception):
            assert await wallet_withdraw_use_case.operation(
                wallet_id=wallet_id, amount=amount
            )
    else:
        assert (
            await wallet_withdraw_use_case.operation(wallet_id=wallet_id, amount=amount)
            == expection
        )
