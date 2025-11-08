from pydantic import BaseModel, EmailStr, validator
from datetime import date
from typing import List
import phonenumbers

# ✅ User schemas
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    phone: str

    @validator("phone")
    def validate_phone(cls, v):
        try:
            parsed = phonenumbers.parse(v, "RW")  # Rwanda region
            if not phonenumbers.is_valid_number(parsed):
                raise ValueError("Invalid phone number")
        except Exception:
            raise ValueError("Invalid phone number format")
        return v

class UserOut(BaseModel):
    id: int
    email: EmailStr
    phone: str

    class Config:
        from_attributes = True

# ✅ Ticket schemas
class TicketCreate(BaseModel):
    numbers: List[int]

class TicketOut(BaseModel):
    id: int
    user_id: int
    numbers: List[int]
    status: str

    class Config:
        from_attributes = True

# ✅ Draw schemas
class DrawCreate(BaseModel):
    date: date
    winning_numbers: List[int]

    class Config:
        from_attributes = True

class DrawOut(BaseModel):
    id: int
    date: date
    winning_numbers: List[int]

    class Config:
        from_attributes = True
