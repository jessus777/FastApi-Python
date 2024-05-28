from src.Infraestructure.db.settings.connection import DBConnectionHandler
from .students_repository import StudentsRepository

def test_insert_student():
    mocked_first_name = 'first'
    mocked_last_name = 'last'
    mocked_age = 30

    students_repository = StudentsRepository()
    students_repository.insert_student(mocked_first_name, mocked_last_name, mocked_age)

    assert True