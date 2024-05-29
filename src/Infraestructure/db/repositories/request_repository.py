from src.Infraestructure.db.settings.connection import  DBConnectionHandler 
from src.Infraestructure.db.entities.requests import Request as RequestEntity
from uuid import uuid4
from sqlalchemy.exc import SQLAlchemyError

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
            except SQLAlchemyError as exception:
                session.rollback()
                print(f"Error occurred while inserting request: {exception}")
                raise Exception
            
    
    @classmethod
    def get_request_by_id(cls, id: str) -> any:
        with DBConnectionHandler() as database:
            session = database.get_session()
            try:
                grimoire = (
                    database.session
                    .query(RequestEntity)
                    .filter_by(id = id)
                    .first()
                    
                )
                return grimoire
            except SQLAlchemyError as exception:
                session.rollback()
                raise Exception(f"Error fetching request by ID: {str(exception)}") 
            
    @classmethod
    def patch_request_status(cls, id: str, status: str) -> None:
        with DBConnectionHandler() as database:
            session = database.get_session()
            try:
                request = (
                    session.query(RequestEntity)
                    .filter_by(id=id)
                    .first()
                )
                if request:
                    request.status = status
                    session.commit()
                else:
                    raise Exception(f"Request with ID {id} not found")
            except SQLAlchemyError as exception:
                session.rollback()
                raise Exception(f"Error updating request status: {str(exception)}")
    
    @classmethod
    def delete_request_by_id(cls, id: str) -> None:
        with DBConnectionHandler() as database:
            session = database.get_session()
            try:
                request = (
                    session.query(RequestEntity)
                    .filter_by(id=id)
                    .first()
                )
                if request:
                    session.delete(request)
                    session.commit()
                else:
                    raise Exception(f"Grimoire with ID {id} not found")
            except Exception as exception:
                session.rollback()
                raise Exception(f"Error deleting grimoire: {str(exception)}")
