from fastapi import FastAPI
from .models import basemodels

app = FastAPI()

@app.get("/")
async def root():
    try:
        return {"status":200, "success": True, "message": "ok", "data": {"greetings":"HELLO WORLD"}}
    except Exception:
        return {"status":500, "success": False, "message": "not ok", "data": []} 

@app.post("/send-feedback/")
async def send_feedback(form: basemodels.FeedbackModel):
    try:
        return {"status":200, "success": True, "message": "ok", "data": form}
    except Exception:
        return {"status":500, "success": False, "message": "not ok", "data": []}