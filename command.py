from abc import abstractmethod, ABC
from typing import List, Any

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

class FirstPrimesCommand(Command):
    def __init__(self, n: int):
        if n < 0:
            raise ValueError
        self._n = n

    def execute(self) -> List[int]:
        n = self._n
        prime_numbers = []
        i = 2
        while len(prime_numbers) < n:
            if self.isPrime(i):
                prime_numbers.append(i)
            i += 1
        return prime_numbers

    def isPrime(self, n) : 
        if (n <= 1) : 
            return False
        if (n <= 3) : 
            return True
    
        if (n % 2 == 0 or n % 3 == 0) : 
            return False
    
        i = 5
        while(i * i <= n) : 
            if (n % i == 0 or n % (i + 2) == 0) : 
                return False
            i = i + 6
    
        return True

class SortAndCombineCommand(Command):
    def __init__(self, first: List[Any], second: List[Any]):
        pass

    def execute(self) -> List[List[str]]:
        return super().execute()
