from contract.observer import Observer
from contract.imodel import IModel


class Model(Observer, IModel):
    __observers: [Observer]
    __messages: [str]

    def __init__(self):
        self.__messages = ["Coucou", "Hey", "Hola", "Hi"]

    def getMessage(self, num: int) -> str:
        if num >= len(self.__messages):
            return "ERROR"
        return self.__messages[num]
