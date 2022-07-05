from sqlalchemy.orm import Session

from ..models import models, schemas

def get_fbs(db: Session):
    return db.query(models.FeedbackModel).all()

def create_fb(db: Session, form: schemas.FeedbackCreate):
    feedback = models.FeedbackModel(**form.dict())
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    return feedback

def update_fb(db:Session, form:dict, id:int):
    db.query(models.FeedbackModel).filter(models.FeedbackModel.id == id).update(form)
    db.commit()
    db.flush()
    return form