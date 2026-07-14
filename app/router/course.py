from fastapi import APIRouter
from schemas.course import Course
import repositories.course as database 

router = APIRouter(prefix="/course", tags=["courses"])

@router.post("")
def create_course(course: Course):
    database.add_course(course.title, course.code, course.credits, course.description)
    return {"message": "Course created successfully"}

@router.get("")
def read_courses():
    rows = database.get_courses()
    return [dict(row) for row in rows]

@router.put("/{course_id}")
def edit_course(course_id: int, course: Course):
    database.update_course(course_id, course.title, course.code, course.credits, course.description)
    return {"message": "Course updated successfully"}

@router.delete("/{course_id}")
def remove_course(course_id: int):
    database.delete_course(course_id)
    return {"message": "Course deleted successfully"}
