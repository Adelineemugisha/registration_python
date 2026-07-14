from fastapi import FastAPI
from app.model import course, student, teacher
from app.router import course as course_router, student as student_router, teacher as teacher_router


app = FastAPI(title="Registration System API")


course.create_table()
student.create_table()
teacher.create_table()
print("Database tables initialized successfully!")


app.include_router(student_router.router)
app.include_router(teacher_router.router)
app.include_router(course_router.router)
