from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from typing import List

from .models import models, schemas
from .db import crud, db_connection, sqls
from .db.database import SessionLocal, engine

import pandas as pd
import numpy as np

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
        return {"status":500, "success": False, "message": "", "data": []} 

@app.post("/send-feedback/")
async def send_feedback(
    form: schemas.FeedbackCreate,
    db: Session = Depends(get_db),
    ):
    try:
        crud.create_fb(db=db, form=form)
        return {"status":200, "success": True, "message": "ok", "data": form}
    except Exception:
        return {"status":500, "success": False, "message": "", "data": []}

@app.get("/feedbacks/")
async def feedbacks(
    db: Session = Depends(get_db)
    ):
    try:
        feedbacks = crud.get_fbs(db=db)
        return {"status":200, "success": True, "message": "ok", "data": feedbacks}
    except Exception:
        return {"status":500, "success": False, "message": "", "data": []}

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
        return {"status":500, "success": False, "message": "", "data": []}

@app.get("/get_sql_query/")
async def get_sql_query():
    try:
        conn = db_connection.connection()
        df = pd.read_sql(sqls.get_all_fbs, conn)
        conn.close()
        return{
            "status":200,
            "success": True,
            "message": "ok",
            "data": df.to_dict("records")
        }
    except Exception as e:
        print(e)
        return {"status":500, "success": False, "message": "", "data": []}