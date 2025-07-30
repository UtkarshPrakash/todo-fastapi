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

class SortItem(BaseModel):
    sort: str
    limit: int

@app.post('/view')
def fetch(req: SortItem):
    orderby = req.sort if req.sort else None
    cnt = req.limit if req.limit else 5
    if orderby.lower() not in ('title', 'description', 'priority', 'status'): orderby = None

    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    order_query = """
        case 
            when priority = 'High' then 1  
            when priority = 'Medium' then 2  
            when priority = 'Low' then 3
        else 4 end as priority_order,
        case
            when status = 'Pending' then 1
            when status = 'InProgress' then 2
            when status = 'Done' then 3
        else 4 end as status_order
    """

    if orderby:
        query = f"SELECT id, title, description, priority, status, {order_query} from todo order by {orderby} limit {cnt};"
    else:
        query = f"SELECT id, title, description, priority, status from todo limit {cnt};"
    
    cursor.execute(query)
    output = cursor.fetchall()
    
    conn.commit()
    conn.close()

    return output

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

    return "Delete successful"
