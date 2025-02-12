import uuid
from typing import cast
from unittest.mock import AsyncMock, Mock

from exceptions.wallet_exceptions import WalletNotFoundError
from tests.unit.mocks.mock_objects import mock_balance_dto
from wallet.application.protocols import WalletOperationsUseCaseProtocol
from schemas.dto.wallet_dto import WalletBalanceDto


async def deposit_operation(
        wallet_id: uuid.UUID,
        amount: float
) -> WalletBalanceDto:
    if wallet_id != mock_balance_dto.wallet_id:
        raise WalletNotFoundError(
                status_code=404,
                detail=f'Wallet {wallet_id!r} not found'
            )
    return mock_balance_dto


async def withdraw_operation(
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

MockWalletWithdrawUseCase = cast(
    WalletOperationsUseCaseProtocol,
    Mock
)


MockWalletDepositUseCase.operation = AsyncMock(
    side_effect=deposit_operation
)

MockWalletWithdrawUseCase.operation = AsyncMock(
    side_effect=withdraw_operation
)