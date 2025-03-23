from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.lib import load_data, get_personalized_meal
import os

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

DATA_PATH = os.path.join("app", "data", "sample_data.csv")
df = load_data(DATA_PATH)

@app.get("/", response_class=HTMLResponse)
def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate", response_class=HTMLResponse)
def generate_plan(request: Request, age: int = Form(...), weight: float = Form(...), preferences: str = Form("")):
    meals = get_personalized_meal(age, weight, preferences, df)
    return templates.TemplateResponse("index.html", {"request": request, "meals": meals})