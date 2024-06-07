from sqlalchemy import Column, Integer

from core.db import DeclarativeBase


class SampleModel(DeclarativeBase):
    __tablename__ = "sample_models"

    id: int = Column(Integer, autoincrement=True, primary_key=True, index=True)
