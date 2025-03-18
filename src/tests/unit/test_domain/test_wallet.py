from decimal import Decimal

from typing import Optional, Type
import pytest

from wallet.domain.wallet import Wallet, WalletDepositError, WalletWithDrawError
import uuid



@pytest.mark.parametrize(
    "wallet, amount, expected, exception",
    [
        (Wallet(id=uuid.uuid4(), balance=Decimal(100)), Decimal(100), Decimal(200), None),
        (Wallet(id=uuid.uuid4(), balance=Decimal(-100)), Decimal(100), 0, None),
        (Wallet(id=uuid.uuid4(), balance=Decimal(100)), Decimal(-100), None, WalletDepositError),
    ],
)
def test_wallet_deposit(
    wallet: Wallet,
    amount: Decimal,
    expected: Optional[Decimal],
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
        (Wallet(id=uuid.uuid4(), balance=Decimal(100)), Decimal(100), 0, None),
        (Wallet(id=uuid.uuid4(), balance=Decimal(0)), Decimal(1), None, WalletWithDrawError),
        (Wallet(id=uuid.uuid4(), balance=Decimal(-1)), Decimal(1), None, WalletWithDrawError),
    ],
)
def test_wallet_withdraw(
    wallet: Wallet,
    amount: Decimal,
    expected: Optional[Decimal],
    exception: Optional[Type[Exception]],
):
    if exception:
        with pytest.raises(exception):
            assert wallet.withdraw(amount)
    else:
        wallet.withdraw(amount)
        assert wallet.balance == expected
