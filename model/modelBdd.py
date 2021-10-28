from contract.observer import Observer
from contract.imodel import IModel
from model.dbconnector import DBConnector


class ModelBDD(Observer, IModel):
    __observers: [Observer]
    __messages: [str]

    def __init__(self):
        self.__dbConnector = DBConnector()

    def getMessage(self, num: int) -> str:
        return self.__dbConnector.getHelloWorldByNum(num)
