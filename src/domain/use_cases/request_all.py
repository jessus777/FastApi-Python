from abc import ABC, abstractmethod
from typing import Dict

class RequestAll(ABC):
    
    @abstractmethod
    def all(self) -> Dict: pass


