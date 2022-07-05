from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from typing import List

from .models import models, schemas
from .db import crud
from .db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    try:
        return {"status":200, "success": True, "message": "ok", "data": {"greetings":"HELLO WORLD"}}
    except Exception:
        return {"status":500, "success": False, "message": "not ok", "data": []} 

@app.post("/send-feedback/")
async def send_feedback(
    form: schemas.FeedbackCreate,
    db: Session = Depends(get_db),
    ):
    try:
        crud.create_fb(db=db, form=form)
        return {"status":200, "success": True, "message": "ok", "data": form}
    except Exception:
        return {"status":500, "success": False, "message": "not ok", "data": []}

@app.get("/feedbacks/")
async def feedbacks(
    db: Session = Depends(get_db)
    ):
    try:
        feedbacks = crud.get_fbs(db=db)
        return {"status":200, "success": True, "message": "ok", "data": feedbacks}
    except Exception:
        return {"status":500, "success": False, "message": "not ok", "data": []}

@app.put("/feedback/{id}")
async def update_fb(
    form: dict,
    id: int,
    db: Session = Depends(get_db),
):
    try:
        fb = crud.update_fb(db=db, form=form ,id=id)
        return{"status":200, "success": True, "message": "ok", "data": fb}
    except Exception as e:
        print(e)
        return {"status":500, "success": False, "message": "not ok", "data": []}