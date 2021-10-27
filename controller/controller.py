from contract.imodel import IModel
from contract.iview import IView
from contract.iactionperformer import IActionPerformer


class Controller(IActionPerformer):
    __view: IView
    __model: IModel

    def setView(self, view: IView) -> None:
        self.__view = view
        view.setActionPerformer(self)
        view.setModel(self.__model)

    def setModel(self, model: IModel) -> None:
        self.__model = model

    def start(self) -> None:
        self.__view.askNum()

    def performUpdateNum(self, num: int) -> None:
        self.__view.showMessage(self.__model.getMessage(num))
