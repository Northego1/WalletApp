from dependency_injector import containers, providers


from WalletApp.src.core.uow import UnitOfWork
from WalletApp.src.core.db import DataBase
from wallet.infrastructure.repository.wallet_repository import WalletRepository
from wallet.application.operation_use_case import (
    WalletDepositUseCase,
    WalletWithDrawUseCase,
)
from schemas.requests.wallet_request_schemes import OperationType
from wallet.application.balance_use_case import WalletGetBalanceUseCase
from api.v1.controllers.wallet.balance import WalletGetBalance
from api.v1.controllers.wallet.operation import WalletOperationController
from WalletApp.src.core.config import settings


class Container(containers.DeclarativeContainer):
    db = providers.Singleton(DataBase, settings.db.dsn)

    unit_of_work = providers.Factory(
        UnitOfWork,
        repository_factory=WalletRepository,
        session_factory=db.provided.engine,
    )

    operations_use_cases = providers.Dict(
        {
            OperationType.DEPOSIT: providers.Factory(
                WalletDepositUseCase,
                uow=unit_of_work,
            ),
            OperationType.WITHDRAW: providers.Factory(
                WalletWithDrawUseCase,
                uow=unit_of_work,
            ),
        }
    )

    wallet_balance_use_case = providers.Factory(
        WalletGetBalanceUseCase, uow=unit_of_work
    )

    wallet_balance_controller = providers.Factory(
        WalletGetBalance, balance_use_case=wallet_balance_use_case
    )

    wallet_operation_controller = providers.Factory(
        WalletOperationController, use_case_operation_dict=operations_use_cases
    )


container = Container()
