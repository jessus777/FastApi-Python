from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from src.Infraestructure.db.settings.base import Base
from .students import Student
import uuid 

class Request(Base):
    __tablename__ = "requests"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey('students.id'), nullable=False)
    status = Column(String, nullable=False)

    # Relationship to Student
    student = relationship("Student")

    def __repr__(self):
        return f"Requests [id={self.id}, student_id={self.student_id}, status={self.status}]"
