import uuid
from schemas.dto.wallet_dto import WalletBalanceDto
from wallet.domain.wallet import Wallet


mock_balance_dto = WalletBalanceDto(
    wallet_id=uuid.UUID("215f91f7-1e8e-4e0f-a751-fdedc03b4ebd"), balance=100
)


mock_wallet_entity = Wallet(
    id=uuid.UUID("215f91f7-1e8e-4e0f-a751-fdedc03b4ebd"), balance=0
)
