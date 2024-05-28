from src.Infraestructure.db.settings.connection import DBConnectionHandler
from .students_repository import StudentsRepository

def test_insert_student():
    mocked_first_name = 'first'
    mocked_last_name = 'last'
    mocked_age = 30

    students_repository = StudentsRepository()
    students_repository.insert_student(mocked_first_name, mocked_last_name, mocked_age)

    assert True

def test_user():
   
    students_repository2 = StudentsRepository()
    response =  students_repository2.get_students()
    print()
    print(response)

def test_user_delete():
    mocked_id = 'E8087158-E9FB-4BA6-80F8-307DC8A300EC'
    students_repository3 = StudentsRepository()
    students_repository3.delete_student_by_id(mocked_id)

    assert True;

def test_user():
   
    students_repository2 = StudentsRepository()
    response =  students_repository2.get_students()
    print()
    print(response)