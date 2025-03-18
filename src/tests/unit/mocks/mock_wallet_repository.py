from unittest.mock import Mock, AsyncMock
from typing import Optional, cast
import uuid

from wallet.domain.wallet import Wallet
from wallet.infrastructure.repository.protocols import WalletRepositoryProtocol
from tests.unit.mocks.mock_objects import mock_wallet_entity


async def get_wallet_by_id(wallet_id: uuid.UUID) -> Optional[Wallet]:
    if wallet_id == mock_wallet_entity.id:
        return Wallet(id=mock_wallet_entity.id, balance=100)


mock_wallet_repository = cast(WalletRepositoryProtocol, Mock())

MockWalletRepository = Mock(
    spec=WalletRepositoryProtocol, return_value=mock_wallet_repository
)

mock_wallet_repository.get_wallet_by_id = AsyncMock(side_effect=get_wallet_by_id)

mock_wallet_repository.update_wallet_balance = AsyncMock(return_value=None)


mock_wallet_repository.get_wallet_for_update = AsyncMock(side_effect=get_wallet_by_id)
