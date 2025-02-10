from api.v1.routes.wallets_routes import router as wallet_router
from fastapi import APIRouter

router = APIRouter()


router.include_router(wallet_router)