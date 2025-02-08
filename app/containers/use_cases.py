from dependency_injector import containers, providers
from app.wallet.application.operation_use_case import WalletDepositUseCase, WalletWithDrawUseCase
from schemas.wallet_request_scheme import OperationType
from wallet.application.balance_use_case import WalletGetBalanceUseCase


class UseCaseContainer(containers.DeclarativeContainer):
    repositories = providers.DependenciesContainer()

    operations_use_cases = providers.Dict(
        {
            OperationType.DEPOSIT: providers.Factory(
                WalletDepositUseCase,
                wallet_repository=repositories.wallet_repository,
            ),
            OperationType.WITHDRAW: providers.Factory(
                WalletWithDrawUseCase,
                wallet_repository=repositories.wallet_repository,
            )
        }
    )

    wallet_balance_use_case = providers.Factory(
        WalletGetBalanceUseCase,
        wallet_repository=repositories.wallet_repository
    )

