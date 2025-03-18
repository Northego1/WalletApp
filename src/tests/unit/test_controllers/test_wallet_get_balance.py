from typing import Optional, Type
import uuid

import pytest
from fastapi import HTTPException

from container import container
from schemas.dto.wallet_dto import WalletBalanceDto
from schemas.responses.wallet_response_schemes import (
    WalletBalanceResponse200,
    WalletBalance,
)
from tests.unit.mocks.mock_objects import mock_balance_dto
from tests.unit.mocks.mock_balance_use_case import MockWalletGetBalance
from dependency_injector import providers
from api.v1.controllers.wallet.balance import WalletGetBalance


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "wallet_id, expection, exception",
    [
        (
            mock_balance_dto.wallet_id,
            WalletBalanceResponse200(
                detail=WalletBalance(
                    wallet_id=mock_balance_dto.wallet_id,
                    balance=mock_balance_dto.balance,
                )
            ),
            None,
        ),
        ("uncorrect data", None, HTTPException),
    ],
)
async def test_wallet_balance_controller(
    wallet_id: uuid.UUID,
    expection: Optional[WalletBalanceDto],
    exception: Optional[Type[Exception]],
):
    container.wallet_balance_controller.override(
        providers.Factory(WalletGetBalance, balance_use_case=MockWalletGetBalance)
    )
    wallet_balance_controller = container.wallet_balance_controller()

    if exception:
        with pytest.raises(exception):
            assert await wallet_balance_controller.get_balance(wallet_id=wallet_id)
    else:
        assert (
            await wallet_balance_controller.get_balance(wallet_id=wallet_id)
            == expection
        )
