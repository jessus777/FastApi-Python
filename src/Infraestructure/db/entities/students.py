from sqlalchemy import Column, String, Integer, UUID
from src.Infraestructure.db.settings.base import Base

class Student(Base):
    __tablename__= "students"

    id = Column(UUID(as_uuid=True), primary_key=True, default=UUID)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    def __repr__(self):
     return f"Students [id={self.id}, first_name={self.first_name}, last_name={self.last_name}, age={self.age}"