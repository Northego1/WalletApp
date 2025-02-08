from dependency_injector import containers, providers
from common.db import engine
from containers.controllers import ControllerContainer
from containers.repositories import RepositoryContainer
from containers.use_cases import UseCaseContainer


class AppContainer(containers.DeclarativeContainer):
    conn = providers.Resource(lambda: engine.connect())

    repositories = providers.Container(RepositoryContainer, conn=conn)
    use_cases = providers.Container(UseCaseContainer, repositories=repositories)
    controller = providers.Container(ControllerContainer, use_cases=use_cases)