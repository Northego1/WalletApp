import sys


print(sys.path, '\n\n\n\n')


from typing import Optional, Type
import pytest

from wallet.domain.wallet import Wallet
import uuid
from exceptions.wallet_exceptions import (
    WalletDepositError,
    WalletWithDrawError
)



@pytest.mark.parametrize(
        "wallet, amount, expected, exception",
        [
            (
                Wallet(id=uuid.uuid4(), balance=100),
                100,
                200,
                None
            ),
            (
                Wallet(id=uuid.uuid4(), balance=-100),
                100,
                0,
                None
            ),
            (
                Wallet(id=uuid.uuid4(), balance=100),
                -100,
                None,
                WalletDepositError
            ), 
        ]
)
def test_wallet_deposit(
    wallet: Wallet,
    amount: float,
    expected: Optional[float],
    exception: Optional[Type[Exception]],
):
    if exception:
        with pytest.raises(exception):
            assert wallet.deposit(amount)
    else:
        wallet.deposit(amount)
        assert wallet.balance == expected



@pytest.mark.parametrize(
        "wallet, amount, expected, exception",
        [
            (
                Wallet(id=uuid.uuid4(), balance=100),
                100,
                0,
                None
            ),
            (
                Wallet(id=uuid.uuid4(), balance=0),
                1,
                None,
                WalletWithDrawError
            ),
            (
                Wallet(id=uuid.uuid4(), balance=-1),
                1,
                None,
                WalletWithDrawError
            ),       
        ]
)
def test_wallet_withdraw(
    wallet: Wallet,
    amount: float,
    expected: Optional[float],
    exception: Optional[Type[Exception]],
):
    if exception:
        with pytest.raises(exception):
            assert wallet.withdraw(amount)
    else:
        wallet.withdraw(amount)
        assert wallet.balance == expected