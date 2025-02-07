from dependency_injector import containers, providers
from wallet.application.wallet_use_cases import WalletDepositUseCase, WalletWithDrawUseCase
from schemas.wallet_request_scheme import OperationType


class Container(containers.DeclarativeContainer):
    operations = providers.Dict(
        {
            OperationType.DEPOSIT: providers.Factory(
                WalletDepositUseCase
            ),
            OperationType.WITHDRAW: providers.Factory(
                WalletWithDrawUseCase
            )
        }
    )