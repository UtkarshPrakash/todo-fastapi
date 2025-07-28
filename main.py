from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

priority_values = ('Low', 'Medium', 'High')
status_values = ('Pending', 'InProgress', 'Done')

class TodoItem(BaseModel):
    title: str
    description: str = None
    priority: str
    status: str
    due_date: str = None

@app.get('/fetch')
def fetch(n: int = 5):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    query = "SELECT id, title, description, priority, status from todo;"
    cursor.execute(query)
    output = cursor.fetchmany(n)
    
    conn.commit()
    conn.close()

    return output

@app.post('/add')
def add_todo(item: TodoItem):
    title = item.title
    description = item.description
    priority = item.priority
    status = item.status

    if priority not in priority_values: raise HTTPException(status_code=401, detail=f"Value should be one of {priority_values}")
    if status not in status_values: raise HTTPException(status_code=401, detail=f"Value should be one of {status_values}")

    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    query = f"""
        INSERT INTO todo 
        (title, description, priority, status, due_date, created_at, updated_at) VALUES
        ('{title}', '{description}', '{priority}', '{status}', '', datetime('now'), datetime('now'));"""

    cursor.execute(query)
    conn.commit()
    conn.close()

@app.post('/remove')
def add_todo(id: int):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    query = f"""DELETE from todo WHERE id = {id}"""

    cursor.execute(query)
    conn.commit()
    conn.close()
