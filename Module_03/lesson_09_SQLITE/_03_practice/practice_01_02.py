import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect(r'databases/users.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        email TEXT NOT NULL
    );
    ''')
        conn.commit()
    except Exception as e:
        print(e)

    try:
        cursor.executemany('''
        INSERT INTO users (name, age, email) VALUES (?, ?, ?)
        ''', [
            ('Иван Иванов', 28, 'ivan@example.com'),
            ('Мария Смирнова', 34, 'maria@example.com'),
            ('Петр Петров', 22, 'peter@example.com'),
            ('Алексей Иванов', 25, 'alexey@example.com'),
            ('Ольга Сидорова', 29, 'olga@example.com')
        ])
        conn.commit()
    except Exception as e:
        print(e)

    try:
        cursor.execute("SELECT * FROM users")
    except Exception as e:
        print(e)
    else:
        users = cursor.fetchall()
        for user in users:
            print(user)

    try:
        cursor.execute("SELECT name, age, email FROM users WHERE age > 25")
    except Exception as e:
        print(e)
    else:
        filtered_users = cursor.fetchall()
        for user in filtered_users:
            print(user)
    print()

    print('Task2')
    try:
        cursor.execute("""
            UPDATE users
            SET age = age + 2
            WHERE user_id = 1;""")

        cursor.execute("""
                UPDATE users
                SET age = age + 3
                WHERE user_id = 4;""")
        conn.commit()
        cursor.execute("SELECT * FROM users")
    except Exception as e:
        print(e)
    else:
        users = cursor.fetchall()
        for user in users:
            print(user)
    print()

    try:
        cursor.execute("""
        DELETE FROM users
        WHERE age < 25
        """)
        conn.commit()
        cursor.execute("SELECT * FROM users")
    except Exception as e:
        print(e)
    else:
        users = cursor.fetchall()
        for user in users:
            print(user)

    conn.close()
