from contract.iview import IView
from contract.imodel import IModel
from contract.iobservable import IObservable
from contract.iactionperformer import IActionPerformer
from contract.observer import Observer


class View(Observer, IView):
    __model: IModel
    __observable: IObservable
    __actionPerformer: IActionPerformer
