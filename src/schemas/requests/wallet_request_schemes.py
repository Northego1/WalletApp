from pydantic import BaseModel
from enum import Enum


class OperationType(str, Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"


class WalletRequestModel(BaseModel):
    operationType: OperationType
    amount: float
