import uuid
from fastapi import APIRouter, Depends

from api.v1.controllers.protocols import WalletGetBalanceControllerProtocol, WalletOperationControllerProtocol
from schemas.requests.wallet_request_schemes import WalletRequestModel
from schemas.responses.wallet_response_schemes import (
    WalletResponse,
    WalletBalanceResponse200,
    WalletBalanceResponse404,
    WalletOperationResponse200,
    WalletOperationResponse400,
    WalletOperationResponse
)
from container import container


router = APIRouter(
    tags=['Wallet'],
    prefix='/api/v1/wallets',
)


@router.post(
        '/{wallet_uuid}/operation',
        responses={
            200: {'model': WalletOperationResponse200},
            400: {'model': WalletOperationResponse400}
        }
)
async def make_wallet_operation(
    wallet_uuid: uuid.UUID,
    wallet_request_dto: WalletRequestModel,
    operation_controller: WalletOperationControllerProtocol = (
        Depends(lambda: container.wallet_operation_controller())
    )
) -> WalletOperationResponse:
    return await operation_controller.operation(
        wallet_id=wallet_uuid,
        wallet_request_dto=wallet_request_dto
    )



@router.get(
        '/{wallet_uuid}',
        responses={
            200: {"model": WalletBalanceResponse200},
            404: {"model": WalletBalanceResponse404},
        }
)
async def get_wallet_balance(
    wallet_uuid: uuid.UUID,
    balance_controller: WalletGetBalanceControllerProtocol = (
        Depends(lambda: container.wallet_balance_controller())
    )
) -> WalletResponse:
    return await balance_controller.get_balance(wallet_id=wallet_uuid)