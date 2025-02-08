from dependency_injector import containers, providers
from wallet.infrastructure.repository.wallet_repository import WalletRepository


class RepositoryContainer(containers.DeclarativeContainer):
    conn = providers.Resource()

    wallet_repository = providers.Factory(
        WalletRepository,
        conn=conn
    )