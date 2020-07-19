from abc import abstractmethod, ABC
from receiver import Receiver
from typing import List, Any

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

class FirstPrimesCommand(Command):
    def __init__(self, n: int, receiver: Receiver):
        pass

    def execute(self) -> List[int]:
        return super().execute()

class SortAndCombineCommand(Command):
    def __init__(self, first: List[Any], second: List[Any], receiver: Receiver):
        pass

    def execute(self) -> List[List[str]]:
        return super().execute()
