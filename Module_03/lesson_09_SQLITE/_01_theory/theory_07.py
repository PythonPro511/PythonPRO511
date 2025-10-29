import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect(r'databases\students.db')
    cursor = conn.cursor()

    cursor.execute("delete from students where age > ?", (21,))
    conn.commit()

    # # просто проверка
    # cursor.execute("SELECT * FROM students;")
    # student = cursor.fetchall()
    # print(student)
    conn.close()
