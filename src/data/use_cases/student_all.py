from typing import Dict
from src.domain.use_cases.student_all import StudentAll as StudentAllInterface
from src.data.interfaces.students_repository import StudentsRepositoryInterface

class StudentAll(StudentAllInterface):
    def __init__(self, student_repository: StudentsRepositoryInterface) -> None:
        self.__student_repository = student_repository

    def all(self) -> Dict:
        self.__student_repository.get_students()
