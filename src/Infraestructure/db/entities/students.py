from sqlalchemy import Column, String, Integer, UUID, ForeignKey
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from src.Infraestructure.db.settings.base import Base
from sqlalchemy.orm import relationship
from .grimoires import Grimoire
import uuid 

class Student(Base):
    __tablename__= "students"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    affinity = Column(String, nullable=False)
    grimoire_id = Column(UUID(as_uuid=True), ForeignKey('grimoires.id'))
    grimoire = relationship('Grimoire')


    def __repr__(self):
     return f"Students [id={self.id}, first_name={self.first_name}, last_name={self.last_name}, age={self.age},  affinity={self.affinity}, grimoire_id = {self.grimoire_id}"