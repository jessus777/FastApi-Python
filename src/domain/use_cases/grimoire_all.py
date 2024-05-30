from abc import ABC, abstractmethod
from typing import Dict

class GrimoireAll(ABC):
    
    @abstractmethod
    def all(self) -> Dict: pass