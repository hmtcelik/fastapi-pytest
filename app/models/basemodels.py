from fastapi import FastAPI

from typing import Union
from pydantic import BaseModel

import datetime


class FeedbackModel(BaseModel):
    title: str
    description: Union[str, None] = None
    date: Union[str, None] = datetime.datetime.now()