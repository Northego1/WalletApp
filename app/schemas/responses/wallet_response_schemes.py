import uuid
from pydantic import BaseModel

class WalletResponse(BaseModel): ...
class WalletOperationResponse(BaseModel): ...
    


class WalletBalance(BaseModel):
    wallet_id: uuid.UUID
    balance: float


class WalletBalanceResponse200(WalletResponse):
    detail: WalletBalance


class WalletBalanceResponse404(WalletResponse):
    detail: str


class WalletOperationResponse200(WalletOperationResponse):
    detail: WalletBalance


class WalletOperationResponse400(WalletOperationResponse):
    detail: str