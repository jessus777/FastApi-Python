from typing import Dict
from src.domain.use_cases.request_all import RequestAll as RequestAllInterface
from src.data.interfaces.request_repository import RequestsRepositoryInterface

class RequestAll(RequestAllInterface):
    def __init__(self, request_repository: RequestsRepositoryInterface) -> None:
        self.__request_repository = request_repository

    def all(self) -> Dict:
        self.__request_repository.get_request_all()
        pass
