from typing import List, Union

from pydantic import BaseModel


class FeedbackBase(BaseModel):
    title: str
    description: str

class FeedbackCreate(FeedbackBase):
    pass

class Feedback(FeedbackBase):
    id: int

    class Config:
        orm_mode = True
        