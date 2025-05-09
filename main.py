from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.lib import generate_answer
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate", response_class=HTMLResponse)
def generate_plan(request: Request, age: int = Form(...), weight: float = Form(...), preferences: str = Form("")):
    query = f"Suggest a meal plan for a {age}-year-old weighing {weight}kg, with preferences: {preferences}"
    answer = generate_answer(query)
    return templates.TemplateResponse("index.html", {"request": request, "meals": answer})
