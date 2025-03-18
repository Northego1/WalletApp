from decimal import Decimal
import uuid
from pydantic import BaseModel


class WalletBalanceDto(BaseModel):
    wallet_id: uuid.UUID
    balance: Decimal


class WalletDto(WalletBalanceDto):
    id: uuid.UUID
