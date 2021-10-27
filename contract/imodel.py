from abc import ABC, abstractmethod


class IModel(ABC):
    @abstractmethod
    def getMessage(self, num: int) -> str:
        ...
