import uuid
from exceptions.wallet_exceptions import WalletNotFoundError
from schemas.requests.wallet_request_schemes import WalletRequestModel
from tests.unit.mocks.mock_objects import mock_balance_dto
from unittest.mock import AsyncMock, Mock
from typing import cast
from wallet.application.protocols import WalletOperationsUseCaseProtocol
from schemas.dto.wallet_dto import WalletBalanceDto


async def wallet_operation(
        wallet_id: uuid.UUID,
        amount: float
) -> WalletBalanceDto:
    if wallet_id != mock_balance_dto.wallet_id:
        raise WalletNotFoundError(
                status_code=404,
                detail=f'Wallet {wallet_id!r} not found'
            )
    return mock_balance_dto


MockWalletDepositUseCase = cast(
    WalletOperationsUseCaseProtocol,
    Mock
)

MockWalletDepositUseCase.operation = AsyncMock(
    side_effect=wallet_operation
)