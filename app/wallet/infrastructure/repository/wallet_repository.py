from typing import Callable, Self
import uuid

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.exc import (
    IntegrityError, 
    DatabaseError
)

from wallet.domain.wallet import Wallet
from exceptions.wallet_exceptions import WalletNotFoundError

class WalletRepository:
    def __init__(self: Self, conn: Callable[..., AsyncConnection]) -> None:
        self.conn_factory = conn
        
        
    async def update_wallet_balance(
            self: Self,
            wallet_id: uuid.UUID,
            new_balance: float
    ):
        async with self.conn_factory() as conn:
            try:
                await conn.execute(text(
                    '''
                        UPDATE wallets
                        SET balance = :new_balance
                        WHERE id = :wallet_id
                    '''
                ), {
                    'new_balance': new_balance,
                    'wallet_id': wallet_id
                })
            except IntegrityError as e:
                pass

            except DatabaseError as e:
                pass
            

    async def get_wallet_by_id(self: Self, wallet_id: uuid.UUID) -> Wallet:
        async with self.conn_factory() as conn:
            try:
                quary_result = await conn.execute(text(
                    '''
                        SELECT *
                        FROM wallets
                        WHERE id = :wallet_id
                    '''
                ),
                {
                    'wallet_id': wallet_id
                }
                )
                row = quary_result.fetchone()
                if not row:
                    raise WalletNotFoundError(
                        status_code=404,
                        detail=f'Wallet {wallet_id!r} not found'
                    )
                return Wallet(id=row[0], balance=row[1])
            
            except IntegrityError as e:
                raise Exception()
            
            except DatabaseError as e:
                raise Exception()