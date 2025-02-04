# models.py
from sqlalchemy import Column, Integer, String
from db import Base

class JobTitle(Base):
    __tablename__ = "job_titles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
