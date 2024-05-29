class Request:
    def __init__(self, student_id: str, status: str) -> None:
        self.student_id = student_id
        self.status = status