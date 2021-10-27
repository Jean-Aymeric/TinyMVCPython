from contract.imodel import IModel
from contract.iview import IView
from contract.iactionperformer import IActionPerformer


class Controller(IActionPerformer):
    __view: IView
    __model: IModel
