import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect(r'databases\students.db')
    cursor = conn.cursor()

    cursor.execute("update students set course = ? where name = ?", ('Информатика', 'Иван Иванов'))
    conn.commit()

    # # просто проверка
    # cursor.execute("SELECT * FROM students;")
    # student = cursor.fetchall()
    # print(student)
    conn.close()
