from abc import ABC, abstractmethod
from typing import Dict

class StudentAll(ABC):

    @abstractmethod
    def all(self) -> Dict: pass