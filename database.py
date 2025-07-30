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

cursor.execute("INSERT INTO todo(title, description, status, priority, created_at, updated_at) VALUES ('Book Ride', 'Ride a book a home', 'Pending', 'Medium', datetime('now'), datetime('now'))")
cursor.execute("INSERT INTO todo(title, description, status, priority, created_at, updated_at) VALUES ('Refuel', 'Get scooty refilled', 'Pending', 'High', datetime('now'), datetime('now'))")
cursor.execute("INSERT INTO todo(title, description, status, priority, created_at, updated_at) VALUES ('Clear Storage', 'Delete some photos from gallery', 'InProgress', 'Low', datetime('now'), datetime('now'))")
cursor.execute("INSERT INTO todo(title, description, status, priority, created_at, updated_at) VALUES ('Lunch', 'Go and eat lunch', 'Done', 'Medium', datetime('now'), datetime('now'))")

conn.commit()

print("Table is ready")

conn.close()
