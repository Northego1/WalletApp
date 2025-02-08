import uuid
from pydantic import BaseModel


class WalletBalanceDto(BaseModel):
    wallet_id: uuid.UUID
    balance: float