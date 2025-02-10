from typing import Self
import uuid

from exceptions.wallet_exceptions import (
    WalletDepositError,
    WalletWithDrawError
)


class Wallet:
    __slots__ = ('id', 'owner_id', '_balance')

    def __init__(
            self: Self,
            id: uuid.UUID,
            balance: float = 0
    ) -> None:
        self.id = id
        self.balance = balance


    @property
    def balance(self: Self) -> float:
        return self._balance
    

    @balance.setter
    def balance(self: Self, value: float):
        self._balance = value


    def deposit(self: Self, amount: float):
        if amount <= 0:
            raise WalletDepositError(
                status_code=400,
                detail="Deposit amount must be positive."
        )
        self.balance += amount


    def withdraw(self: Self, amount: float):
        if self.balance <= 0:
            raise WalletWithDrawError(
                status_code=400,
                detail='Impossible to withdraw, the balance less or equal 0.'
            )
        if self.balance < amount:
            raise WalletWithDrawError(
                status_code=400,
                detail='Impossible to withdraw, the balance is less than the amount.'
            )
        self.balance -= amount
        