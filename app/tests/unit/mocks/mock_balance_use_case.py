import uuid
from typing import cast
from unittest.mock import AsyncMock, Mock

from exceptions.wallet_exceptions import WalletNotFoundError
from tests.unit.mocks.mock_objects import mock_balance_dto
from wallet.application.protocols import WalletGetBalanceUseCaseProtocol
from schemas.dto.wallet_dto import WalletBalanceDto
from schemas.requests.wallet_request_schemes import WalletRequestModel


async def get_wallet_side_effect(
        wallet_id: uuid.UUID,
) -> WalletBalanceDto:
    if mock_balance_dto.wallet_id != wallet_id:
        raise WalletNotFoundError(
                status_code=404,
                detail=f'Wallet {wallet_id!r} not found'
            )
    return mock_balance_dto


MockWalletGetBalance = cast(
    WalletGetBalanceUseCaseProtocol,
    Mock
)

MockWalletGetBalance.get_wallet_balance = AsyncMock(
    side_effect=get_wallet_side_effect
)