from typing import Self
import uuid

from app.api.wallet.domain.wallet import Wallet


class User:
    __slots__ = ('id', 'name', 'email', 'wallet')


    def __init__(
            self: Self,
            id: uuid.UUID,
            name: str,
            email: str,
            wallet: Wallet
    ) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.wallet = wallet


