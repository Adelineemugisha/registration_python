# import sqlite3
# from contextlib import contextmanager

# sqlite_file_name = "school.db"

# @contextmanager
# def get_connection():
#     connection = sqlite3.connect(sqlite_file_name)
#     connection.row_factory = sqlite3.row
#     try:
#         yield connection
#         connection.commit()
#     finally:
#         connection.close()

# def create_table():
#     with get_connection() as connection:
#         connection.execute('''CREATE TABLE IF NOT EXISTTS students(
#         id INTEGER PRIMARY KEY AUTHOINCREMENT,
#         name TEXT NOT NULL,
#         age INTEGER NOT NULL,
#         email TEXT NOT NULL,
#         country TEXT NOT NULL,
#         id_number INTEGER NOT NULL
#         )''')

# def add_student(name, age, email, country, id_number):
#     with get_connection() as connection:
#         connection.execute(

#             'INSERT INTO students (name, age, email, country, id_number) VALUES (?, ?, ?, ?, ?)',
#             (name, age, email, country, id_number),
#         )

# def get_students():
#     with get_connection() as connection:
#         return connection.execute('SELECT * FROM students').fetchall()

# def get_students 
