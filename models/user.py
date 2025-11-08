from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base  # This should match your db.py setup

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, index=True, nullable=False)

    tickets = relationship("Ticket", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"
