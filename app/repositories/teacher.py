from app.database import get_db_connection


def add_teacher(first_name, last_name, email, department):
    with get_connection() as connection:
        connection.execute('INSERT INTO teachers (first_name, last_name, email, department) VALUES (?, ?, ?, ?)',
                           (first_name, last_name, email, department))
        connection.commit()

def get_teachers():
    with get_connection() as connection:
        return connection.execute('SELECT * FROM teachers').fetchall()

def update_teacher(teacher_id, first_name, last_name, email, department):
    with get_connection() as connection:
        connection.execute('UPDATE teachers SET first_name=?, last_name=?, email=?, department=? WHERE id=?',
                           (first_name, last_name, email, department, teacher_id))
        connection.commit()

def delete_teacher(teacher_id):
    with get_connection() as connection:
        connection.execute('DELETE FROM teachers WHERE id=?', (teacher_id,))
        connection.commit()
