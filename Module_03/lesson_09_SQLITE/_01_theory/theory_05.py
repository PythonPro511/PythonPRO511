import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect(r'databases\students.db')
    cursor = conn.cursor()

    # fetchall() — получает все строки из результата запроса.
    cursor.execute("SELECT * FROM students WHERE course = ?", ('Химия',))
    math_studs = cursor.fetchall()

    print(math_studs)

    conn.close()
