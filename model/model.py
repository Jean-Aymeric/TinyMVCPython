from contract.observer import Observer
from contract.imodel import IModel


class Model(Observer, IModel):
    __observers: [Observer]
