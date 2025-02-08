from typing import Self


class WalletError(Exception):
    def __init__(
            self: Self,
            status_code: int = 400,
            detail: str = 'Unkonwn wallet error',
            *args: object
    ) -> None:
        self.detail = detail
        self.status_code = status_code
        super().__init__(*args)


class WalletDepositError(WalletError):
    pass


class WalletWithDrawError(WalletError):
    pass


class WalletNotFoundError(WalletError):
    pass