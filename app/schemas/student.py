from pydantic import BaseModel

class Student(BaseModel):
    first_name: str
    last_name: str
    email: str
    enrollment_date: str
