from typing import Optional, Type
import uuid

import pytest
from dependency_injector import providers

from common.uow import UnitOfWork
from container import container
from exceptions.wallet_exceptions import WalletNotFoundError
from schemas.dto.wallet_dto import WalletBalanceDto
from tests.unit.mocks.mock_objects import mock_balance_dto
from wallet.application.balance_use_case import WalletGetBalanceUseCase
from tests.unit.mocks.mock_wallet_repository import MockWalletRepository
from tests.unit.mocks.mock_db_session import MockSession

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "wallet_id, expection, exception",
    [
        (
            mock_balance_dto.wallet_id,
            mock_balance_dto,
            None
        ),
        (
            "uncorrect data",
            None,
            WalletNotFoundError
        )
    ]
)
async def test_wallet_deposit_use_case(
    wallet_id: uuid.UUID,
    expection: Optional[WalletBalanceDto],
    exception: Optional[Type[Exception]]
):
    container.wallet_balance_use_case.override(
        providers.Factory(
            WalletGetBalanceUseCase,
            uow=providers.Factory(
                UnitOfWork,
                repository_factory=MockWalletRepository,
                session_factory=MockSession
            )
        )
    )
    wallet_balance_use_case = container.wallet_balance_use_case()

    if exception:
        with pytest.raises(exception):
            assert await wallet_balance_use_case.get_wallet_balance(
                wallet_id=wallet_id, 
            )
    else:
        assert await wallet_balance_use_case.get_wallet_balance(
            wallet_id=wallet_id, 
        ) == expection







