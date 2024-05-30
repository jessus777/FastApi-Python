from abc import ABC, abstractmethod
from typing import List
from src.domain.models.students import Students

class StudentsRepositoryInterface(ABC):
    @abstractmethod
    def insert_student(cls, first_name: str, last_name: str, age: int, affinity: str, grimoire_id: str) -> None: pass

    @abstractmethod
    def get_students(cls) -> List[Students] : pass

    @abstractmethod
    def delete_student_by_id(cls, id: str) -> None: pass