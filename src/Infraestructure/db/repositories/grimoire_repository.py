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
