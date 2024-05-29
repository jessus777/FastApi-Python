from src.Infraestructure.db.settings.connection import DBConnectionHandler
from .request_repository import RequestsRepository

def test_insert_request():
    mocked_student_id = '329AC79A-A085-4C6F-A5A2-94541C6A88B8'
    mocked_status = "pendiente"

    students_repository = RequestsRepository()
    students_repository.insert_request(mocked_student_id, mocked_status)

    assert True