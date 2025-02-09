from dependency_injector import containers, providers


from common.db import DataBase
from wallet.infrastructure.repository.wallet_repository import WalletRepository
from wallet.application.operation_use_case import WalletDepositUseCase, WalletWithDrawUseCase
from schemas.wallet_request_scheme import OperationType
from wallet.application.balance_use_case import WalletGetBalanceUseCase
from api.v1.controllers.wallet.balance import WalletGetBalance
from api.v1.controllers.wallet.operation import WalletOperationController
from config import settings


class Container(containers.DeclarativeContainer):
    db = providers.Singleton(DataBase, settings.db.dsn)

    wallet_repository = providers.Factory(
        WalletRepository,
        conn=db.provided.connection
    )


    operations_use_cases = providers.Dict(
        {
            OperationType.DEPOSIT: providers.Factory(
                WalletDepositUseCase,
                wallet_repository=wallet_repository,
            ),
            OperationType.WITHDRAW: providers.Factory(
                WalletWithDrawUseCase,
                wallet_repository=wallet_repository,
            )
        }
    )

    wallet_balance_use_case = providers.Factory(
        WalletGetBalanceUseCase,
        wallet_repository=wallet_repository
    )


    wallet_balance_controller = providers.Factory(
        WalletGetBalance,
        balance_use_case=wallet_balance_use_case
    )

    wallet_operation_controller = providers.Factory(
        WalletOperationController,
        use_case_operation_dict=operations_use_cases
    )


container = Container()
