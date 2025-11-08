from pydantic import BaseModel, EmailStr
from datetime import date
from typing import List, Optional

# User-related schemas
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True

# Ticket-related schemas
class TicketCreate(BaseModel):
    numbers: List[int]

class TicketOut(BaseModel):
    id: int
    user_id: int
    numbers: List[int]
    status: str

    class Config:
        orm_mode = True

# Draw-related schemas
class DrawCreate(BaseModel):
    date: date
    winning_numbers: List[int]

    class Config:
        orm_mode = True

class DrawOut(BaseModel):
    id: int
    date: date
    winning_numbers: List[int]

    class Config:
        orm_mode = True
