from decimal import Decimal
from typing import Optional, Self
import uuid

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.exc import IntegrityError, DatabaseError

from wallet.domain.wallet import Wallet


class WalletRepository:
    def __init__(self: Self, conn: AsyncConnection) -> None:
        self.conn = conn

    async def update_wallet_balance(
        self: Self, wallet_id: uuid.UUID, new_balance: Decimal
    ):
        try:
            await self.conn.execute(
                text(
                    """
                    UPDATE wallets
                    SET balance = :new_balance
                    WHERE id = :wallet_id
                """
                ),
                {"new_balance": new_balance, "wallet_id": wallet_id},
            )
        except IntegrityError as e:
            pass

        except DatabaseError as e:
            pass


    async def get_wallet_for_update(
        self: Self, wallet_id: uuid.UUID
    ) -> Optional[Wallet]:
        try:
            quary_result = await self.conn.execute(
                text(
                    """
                    SELECT *
                    FROM wallets
                    WHERE id = :wallet_id
                    FOR UPDATE
                """
                ),
                {"wallet_id": wallet_id},
            )
            row = quary_result.fetchone()
            if not row:
                return None
            return Wallet(id=row[0], balance=row[1])

        except IntegrityError as e:
            raise Exception()

        except DatabaseError as e:
            raise Exception()


    async def get_wallet_by_id(self: Self, wallet_id: uuid.UUID) -> Optional[Wallet]:
        try:
            quary_result = await self.conn.execute(
                text(
                    """
                    SELECT *
                    FROM wallets
                    WHERE id = :wallet_id
                """
                ),
                {"wallet_id": wallet_id},
            )
            row = quary_result.fetchone()
            if not row:
                return None
            return Wallet(id=row[0], balance=row[1])

        except IntegrityError as e:
            raise Exception()

        except DatabaseError as e:
            raise Exception()
