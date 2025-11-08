from sqlalchemy import Column, Integer, Date, String
from db import Base

class Draw(Base):
    __tablename__ = "draws"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    winning_numbers = Column(String, nullable=False)  # Stored as comma-separated string
