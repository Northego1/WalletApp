from pydantic import BaseModel
from enum import Enum


class OperationType(str, Enum):
    DEPOSIT = 'DEPOSIT'
    WITHDRAW = 'WITHDRAW'


class WalletRequestDto(BaseModel):
    operationType: OperationType
    amount: float