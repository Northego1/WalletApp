import uuid
from fastapi import APIRouter, Depends

from api.v1.controllers.protocols import WalletGetBalanceControllerProtocol
from schemas.wallet_request_scheme import WalletRequestDto
from container import container


router = APIRouter(
    tags=['Wallet'],
    prefix='/api/v1/wallets',
)


@router.post('/{wallet_uuid}/operation')
async def make_wallet_operation(
    wallet_uuid: uuid.UUID,
    wallet_request_dto: WalletRequestDto,
    operation_controller = Depends(lambda: container.wallet_operation_controller())
):
    ...


@router.get('/{wallet_uuid}')
async def get_wallet_balance(
    wallet_uuid: uuid.UUID,
    balance_controller: WalletGetBalanceControllerProtocol = (
        Depends(lambda: container.wallet_balance_controller())
    )
):
    return await balance_controller.get_balance(wallet_id=wallet_uuid)