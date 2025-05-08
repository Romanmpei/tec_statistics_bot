from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from collections import Counter
from src.db import SessionLocal, UserAction
from datetime import datetime

app = FastAPI()
templates = Jinja2Templates(directory="src/templates")

@app.get("/", response_class=HTMLResponse)
async def analytics(request: Request):
    db = SessionLocal()
    actions = db.query(UserAction).all()
    db.close()

    total_actions = len(actions)
    unique_users = len(set(a.user_id for a in actions))

    category_counts = Counter(a.category for a in actions if a.action == "select_category")
    year_counts = Counter(a.year for a in actions if a.action == "select_year")

    return templates.TemplateResponse("analytics.html", {
        "request": request,
        "total_actions": total_actions,
        "unique_users": unique_users,
        "category_counts": category_counts.items(),
        "year_counts": year_counts.items(),
    })
