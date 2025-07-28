import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS todo;")

create_table = """
    CREATE TABLE todo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT ,
        status VARCHAR(255) NOT NULL,
        priority VARCHAR(255) NOT NULL,
        due_date TEXT,
        created_at TEXT,
        updated_at TEXT
    );
"""

cursor.execute(create_table)

def insert_query(n: int):
    query = f"""INSERT INTO todo (
                    title, description, status, priority, 
                    due_date, created_at, updated_at ) 
               VALUES (
                    'Test{n}', 'This is description {n}', 'Pending', 
                    'Medium', '', datetime('now'), datetime('now'));
            """
    return query

cursor.execute(insert_query(1))
cursor.execute(insert_query(2))
cursor.execute(insert_query(3))

conn.commit()

print("Table is ready")

conn.close()