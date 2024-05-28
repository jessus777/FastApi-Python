from src.Infraestructure.db.settings.connection import DBConnectionHandler
from .students_repository import StudentsRepository

def test_insert_student():
    mocked_first_name = 'first'
    mocked_last_name = 'last'
    mocked_age = 30
    mocked_affinity  = 'lastnext'
    mocked_grimoire_id = '7489729E-9FBD-4627-A850-D3DD447C7E8A'

    students_repository = StudentsRepository()
    students_repository.insert_student(mocked_first_name, mocked_last_name, mocked_age, mocked_affinity, mocked_grimoire_id)

    assert True

