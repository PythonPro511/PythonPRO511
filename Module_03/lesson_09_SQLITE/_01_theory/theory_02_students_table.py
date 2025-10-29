import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect(r'databases\students.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            course TEXT
        )
        ''')
    # cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
    #                ("Иван Иванов", 20, "Математика"))
    # cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
    #                ("Анна Смирнова", 22, "Физика"))
    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
                   ("Дмитрий Леонов", 23, "Химия"))

    conn.commit()
    conn.close()
