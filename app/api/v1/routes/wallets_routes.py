import uuid
from fastapi import APIRouter

from schemas.wallet_request_scheme import WalletRequestDto



router = APIRouter(
    tags=['Wallet'],
    prefix='/api/v1/wallets'
)


@router.post('/{wallet_uuid}/operation')
async def make_wallet_operation(
    wallet_uuid: uuid.UUID,
    wallet_request_dto: WalletRequestDto
):
    pass


@router.get('/{wallet_uuid}')
async def get_wallet_balance(
    wallet_uuid: uuid.UUID
)