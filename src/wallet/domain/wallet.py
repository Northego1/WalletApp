from decimal import Decimal
from typing import Self
import uuid

from WalletApp.src.core.wallet_exceptions import WalletError


class WalletDepositError(WalletError): ...


class WalletWithDrawError(WalletError): ...


class WalletNotFoundError(WalletError): ...


class Wallet:
    __slots__ = ("id", "owner_id", "_balance")

    def __init__(self: Self, id: uuid.UUID, balance: Decimal = Decimal(0)) -> None:
        self.id = id
        self.balance = balance

    @property
    def balance(self: Self) -> Decimal:
        return self._balance

    @balance.setter
    def balance(self: Self, value: Decimal):
        self._balance = value

    def deposit(self: Self, amount: Decimal):
        if amount <= 0:
            raise WalletDepositError(
                status_code=400, detail="Deposit amount must be positive."
            )
        self.balance += amount

    def withdraw(self: Self, amount: Decimal):
        if self.balance <= 0:
            raise WalletWithDrawError(
                status_code=400,
                detail="Impossible to withdraw, the balance less or equal 0.",
            )
        if self.balance < amount:
            raise WalletWithDrawError(
                status_code=400,
                detail="Impossible to withdraw, the balance is less than the amount.",
            )
        self.balance -= amount
