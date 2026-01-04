from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import db, schema

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Initialize DB at startup
schema.init_db()

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    conn = db.get_db()
    cursor = conn.cursor()

    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM users WHERE username=? AND password=?"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    return {"message": "Login success" if user else "Invalid credentials"}
