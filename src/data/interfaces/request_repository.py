from abc import ABC, abstractmethod
from typing import List
from src.domain.models.request import Request

class RequestsRepositoryInterface(ABC):

    @abstractmethod
    def insert_request(self, student_id: str, status: str) -> None: pass

    @abstractmethod    
    def get_request_by_id(self, id: str) -> any: pass 

    @abstractmethod        
    def patch_request_status(self, id: str, status: str) -> None: pass
    
    @abstractmethod
    def delete_request_by_id(self, id: str) -> None: pass
    
    @abstractmethod
    def get_request_all(cls) -> List[Request]: pass

