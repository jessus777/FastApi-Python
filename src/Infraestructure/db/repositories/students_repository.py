from src.Infraestructure.db.settings.connection import  DBConnectionHandler 
from src.Infraestructure.db.entities.students import Student as StudentsEntity
from uuid import uuid4

class StudentsRepository:

    @classmethod
    def insert_student(cls, first_name: str, last_name: str, age: int, affinity: str, grimoire_id: str) -> None: 
        with DBConnectionHandler() as database:
            session = database.get_session()
            try:
                new_registry = StudentsEntity(
                    id = uuid4(),
                   first_name = first_name, 
                   last_name = last_name,
                   age = age ,
                   affinity = affinity,
                   grimoire_id = grimoire_id
                )
                session.add(new_registry)
                session.commit()
            except Exception as exception:
                session.rollback()
                print(f"Error occurred while inserting student: {exception}")
                raise Exception


    @classmethod
    def get_students(cls) -> any:
        with DBConnectionHandler() as database:
            session = database.get_session()
            try:
                students = (
                    session
                    .query(StudentsEntity)
                    .all()

                )
                return students
            except Exception as exception:
                session.rollback()
                raise Exception 
            
    @classmethod
    def delete_student_by_id(cls, id: str) -> None:
        with DBConnectionHandler() as database:
            session = database.get_session()
            try:
                student_to_delete = (
                    session
                    .query(StudentsEntity)
                    .filter_by(id = id)
                    .first()
                )
                if student_to_delete:
                    session.delete(student_to_delete)
                    session.commit()

            except Exception as exception:
                session.rollback()
                raise Exception 

