from src.Infraestructure.db.settings.connection import  DBConnectionHandler 
from src.Infraestructure.db.entities.students import Student as StudentsEntity
from uuid import uuid4

class StudentsRepository:

    @classmethod
    def insert_student(cls, first_name: str, last_name: str, age: int) -> None: 
        with DBConnectionHandler() as database:
            session = database.get_session()
            try:
                new_registry = StudentsEntity(
                    id = uuid4(),
                   first_name = first_name, 
                   last_name = last_name,
                   age = age     
                )
                session.add(new_registry)
                session.commit()
            except Exception as exception:
                session.rollback()
                raise Exception
