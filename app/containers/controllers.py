from dependency_injector import containers, providers

from app.api.v1.controllers.wallet.balance import WalletGetBalance
from app.api.v1.controllers.wallet.operation import WalletOperationController


class ControllerContainer(containers.DeclarativeContainer):
    use_cases = providers.DependenciesContainer()

    wallet_balance_controller = providers.Factory(
        WalletGetBalance,
        balance_use_case=use_cases.wallet_balance_use_case
    )

    wallet_operation_controller = providers.Factory(
        WalletOperationController,
        use_case_operation_dict=use_cases.operations_use_cases
    )

