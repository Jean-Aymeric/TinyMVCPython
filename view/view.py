from contract.iview import IView
from contract.imodel import IModel
from contract.iobservable import IObservable
from contract.iactionperformer import IActionPerformer
from contract.observer import Observer


class View(Observer, IView):
    __model: IModel
    __observable: IObservable
    __actionPerformer: IActionPerformer

    def setActionPerformer(self, actionPerformer: IActionPerformer) -> None:
        self.__actionPerformer = actionPerformer

    def setModel(self, model: IModel) -> None:
        self.__model = model

    def showMessage(self, message: str) -> None:
        print(message)

    def askNum(self) -> int:
        while(True):
            print("Entrez un numéro :")
            self.__actionPerformer.performUpdateNum(int(input()))
