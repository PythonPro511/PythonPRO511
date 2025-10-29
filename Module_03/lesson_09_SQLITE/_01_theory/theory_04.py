import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect(r'databases\students.db')
    cursor = conn.cursor()

    # fetchall() — получает все строки из результата запроса.
    cursor.execute("SELECT * FROM students;")
    students = cursor.fetchall()
    print(students)

    for id_, name, age, course in students:
        print(f'id - {id_}, name - {name}, age - {age}, course - {course}')
    print()

    # Метод fetchone() возвращает первую строку результата запроса в виде кортежа.
    # Если строк больше нет, возвращается None.
    cursor.execute("SELECT * FROM students;")
    student = cursor.fetchone()
    print(student)
    student = cursor.fetchone()
    print(student)
    print()

    # fetchmany(n) — получает n строк из результата запроса.
    cursor.execute("SELECT * FROM students;")
    while True:
        rows = cursor.fetchmany(2)
        if not rows:
            break
        print(rows)


    conn.close()
