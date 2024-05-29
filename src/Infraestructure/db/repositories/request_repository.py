from src.Infraestructure.db.settings.connection import  DBConnectionHandler 
from src.Infraestructure.db.entities.requests import Request as RequestEntity
from uuid import uuid4

class RequestsRepository:
    @classmethod
    def insert_request(cls, student_id: str, status: str) -> None: 
        with DBConnectionHandler() as database:
            session = database.get_session()
            try:
                new_registry = RequestEntity(
                    id = uuid4(),
                    student_id = student_id,
                    status = status                   
                )
                session.add(new_registry)
                session.commit()
            except Exception as exception:
                session.rollback()
                print(f"Error occurred while inserting student: {exception}")
                raise Exception