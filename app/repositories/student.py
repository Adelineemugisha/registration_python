from app.database import get_db_connection

def add_student(first_name, last_name, email, enrollment_date):
    with get_db_connection() as connection:
        connection.execute(
            'INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (?, ?, ?, ?)',
            (first_name, last_name, email, enrollment_date)
        )
        connection.commit()

def get_students():
    with get_db_connection() as connection:
        return connection.execute('SELECT * FROM students').fetchall()

def update_student(student_id, first_name, last_name, email, enrollment_date):
    with get_db_connection() as connection:
        connection.execute(
            'UPDATE students SET first_name=?, last_name=?, email=?, enrollment_date=? WHERE id=?',
            (first_name, last_name, email, enrollment_date, student_id)
        )
        connection.commit()

def delete_student(student_id):
    with get_db_connection() as connection:
        connection.execute('DELETE FROM students WHERE id=?', (student_id,))
        connection.commit()
