from abc import ABC, abstractmethod


class IActionPerformer(ABC):
    @abstractmethod
    def performUpdateNum(self, num: int) -> None:
        ...
