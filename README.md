### Requirements
- Basic todo list
- Add priority, due date
- Fetch sorted by priority or urgency
- Status field (pending, in progress, done)

### Stack
- **Language**: Python
- **Framework**: FastAPI
- **DB**: SQLite (via SQLAlchemy or Tortoise ORM)
- **Testing Tool**: Swagger UI (auto in FastAPI) or Postman
- **Auth**: Optional (start without, add later if time)

### Schema
- `id`: int (primary key)
- `title`: str
- `description`: str (optional)
- `status`: enum ("pending", "in_progress", "done")
- `priority`: enum ("low", "medium", "high")
- `due_date`: datetime (optional)
- `created_at`: datetime
- `updated_at`: datetime

### Core Endpoints
1. **POST /todos**
    - Create new todo
    - Input: title, description, priority, due_date
    - Output: full todo object
2. **GET /todos**
    - List all todos
    - Optional filters: status, priority
    - Sort: by due_date or priority
3. **GET /todos/{id}**
    - Fetch specific todo
4. **PUT /todos/{id}**
    - Update title, status, priority, etc.
5. **DELETE /todos/{id}**
    - Delete todo

### Folder Structure
```text
todo_api/
│
├── main.py
├── models.py
├── schemas.py
├── database.py
├── crud.py
└── requirements.txt
```

### Running the app
The app can be launched locally using uvicorn
```bash
cd C:\DATA\fastapi\todo_api
uvicorn main:app --reload
```