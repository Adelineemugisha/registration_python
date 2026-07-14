from fastapi import APIRouter
from schemas.teacher import Teacher
import repositories.teacher as repo

router = APIRouter(prefix="/teacher", tags=["teachers"])

@router.post("")
def create_teacher(teacher: Teacher):
    repo.add_teacher(teacher.first_name, teacher.last_name, teacher.email, teacher.department)
    return {"message": "Teacher created successfully"}

@router.get("")
def read_teachers():
    rows = repo.get_teachers()
    return [dict(row) for row in rows]

@router.put("/{teacher_id}")
def edit_teacher(teacher_id: int, teacher: Teacher):
    repo.update_teacher(teacher_id, teacher.first_name, teacher.last_name, teacher.email, teacher.department)
    return {"message": "Teacher updated successfully"}

@router.delete("/{teacher_id}")
def remove_teacher(teacher_id: int):
    repo.delete_teacher(teacher_id)
    return {"message": "Teacher deleted successfully"}
