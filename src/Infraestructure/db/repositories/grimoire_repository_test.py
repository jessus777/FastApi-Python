from src.Infraestructure.db.settings.connection import DBConnectionHandler
from .grimoire_repository import GrimoiresRepository

def test_insert_grimoires():
    mocked_name = 'first'
    mocked_level = 1

    students_repository = GrimoiresRepository()
    students_repository.insert_grimoires(mocked_name, mocked_level)

    assert True

