from src.Infraestructure.db.settings.connection import  DBConnectionHandler 
from src.Infraestructure.db.entities.grimoires import Grimoire as GrimoireEntity
from uuid import uuid4

class GrimoiresRepository:
    @classmethod 
    def insert_grimoires(cls, name: str, level: int) -> None: 
        with DBConnectionHandler() as database:
            session = database.get_session()
            try:
                new_registry = GrimoireEntity(
                    id = uuid4(),
                    name = name,
                    level = level
                )
                session.add(new_registry)
                session.commit()
            except Exception as exception:
                session.rollback()
                raise Exception
            
            
    @classmethod
    def get_grimoires_by_id(cls, id: str) -> any:
        with DBConnectionHandler() as database:
            session = database.get_session()
            try:
                grimoire = (
                    database.session
                    .query(GrimoireEntity)
                    .filter_by(id = id)
                    .first()
                    
                )
                return grimoire
            except Exception as exception:
                session.rollback()
                raise Exception(f"Error fetching grimoire by ID: {str(exception)}")  
            
            
    @classmethod
    def get_grimoires_list(cls) -> any:
        with DBConnectionHandler() as database:
            session = database.get_session()
            try:
                grimoires = (
                    database.session
                    .query(GrimoireEntity)
                    .all()
                    
                )
                return grimoires
            except Exception as exception:
                session.rollback()
                raise Exception(f"Error fetching grimoire all: {str(exception)}") 
            
            
    @classmethod
    def delete_grimoire_by_id(cls, id: str) -> None:
        with DBConnectionHandler() as database:
            session = database.get_session()
            try:
                grimoire = (
                    session.query(GrimoireEntity)
                    .filter_by(id=id)
                    .first()
                )
                if grimoire:
                    session.delete(grimoire)
                    session.commit()
                else:
                    raise Exception(f"Grimoire with ID {id} not found")
            except Exception as exception:
                session.rollback()
                raise Exception(f"Error deleting grimoire: {str(exception)}")
