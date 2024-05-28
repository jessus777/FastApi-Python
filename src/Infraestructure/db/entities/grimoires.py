from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from src.Infraestructure.db.settings.base import Base
import uuid 

class Grimoire(Base):
    __tablename__ = "grimoires"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    level = Column(Integer, nullable=False)
 

    def __repr__(self):
        return f"Grimoires [id={self.id}, name={self.name}, level={self.level}]"