from typing import Self
import uuid


class WalletError(Exception):
    def __init__(
        self: Self,
        status_code: int = 400,
        detail: str = "Unknown wallet error",
        *args: object,
    ) -> None:
        self.detail = detail
        self.status_code = status_code
        super().__init__(*args)
