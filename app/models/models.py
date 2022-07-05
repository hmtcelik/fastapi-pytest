from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..db.database import Base


class FeedbackModel(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description= Column(String, index=True)
