from contract.observer import Observer
from contract.imodel import IModel
import json


class ModelJSON(Observer, IModel):
    __observers: [Observer]
    __messages: [str]

    def __init__(self):
        self.__loadMessages()

    def getMessage(self, num: int) -> str:
        return self.__messages[str(num)]

    def __loadMessages(self):
        with open('conf/messages.json') as messageFile:
            self.__messages = json.load(messageFile)
