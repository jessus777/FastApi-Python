from abc import ABC, abstractmethod
from typing import List
from src.domain.models.grimorios import Grimoires

class GrimoiresRepositoryInterface(ABC):
    @abstractmethod 
    def insert_grimoires(cls, name: str, level: int) -> None: pass
    @abstractmethod
    def get_grimoires_by_id(cls, id: str) -> any: pass
            
    @abstractmethod
    def get_grimoires_list(cls) -> List[Grimoires]: pass
            
    @abstractmethod
    def delete_grimoire_by_id(cls, id: str) -> None: pass