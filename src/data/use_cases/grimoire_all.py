from typing import Dict
from src.domain.use_cases.grimoire_all import GrimoireAll as GrimoireAllInterface
from src.data.interfaces.grimoire_repository import GrimoiresRepositoryInterface

class GrimoireAll(GrimoireAllInterface):
    def __init__(self, grimoire_repository: GrimoiresRepositoryInterface) -> None:
        self.__grimoire_repository = grimoire_repository

    def all(self) -> Dict:
        self.__grimoire_repository.get_grimoires_list()
        pass