from fastapi import APIRouter
from schemas.student import Student
import repositories.student as repo

router = APIRouter(prefix="/student", tags=["students"])

@router.post("")
def create_student(student: Student):
    repo.add_student(student.first_name, student.last_name, student.email, student.enrollment_date)
    return {"message": "Student created successfully"}

@router.get("")
def read_students():
    rows = repo.get_students()
    return [dict(row) for row in rows]

@router.put("/{student_id}")
def edit_student(student_id: int, student: Student):
    repo.update_student(student_id, student.first_name, student.last_name, student.email, student.enrollment_date)
    return {"message": "Student updated successfully"}

@router.delete("/{student_id}")
def remove_student(student_id: int):
    repo.delete_student(student_id)
    return {"message": "Student deleted successfully"}

