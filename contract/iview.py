from abc import ABC, abstractmethod
from contract.iactionperformer import IActionPerformer
from contract.imodel import IModel


class IView(ABC):
    @abstractmethod
    def showMessage(self, message: str) -> None:
        ...

    @abstractmethod
    def setActionPerformer(self, actionPerformer: IActionPerformer) -> None:
        ...

    @abstractmethod
    def setModel(self, model: IModel) -> None:
        ...