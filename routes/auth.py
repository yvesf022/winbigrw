from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models.user import User
from utils.otp import generate_otp

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(phone: str, db: Session = Depends(get_db)):
    otp = generate_otp()
    user = User(phone=phone, otp=otp)
    db.add(user)
    db.commit()
    return {"message": "OTP yoherejwe", "otp": otp}

@router.post("/verify-otp")
def verify(phone: str, otp: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.phone == phone).first()
    if user and user.otp == otp:
        user.verified = True
        db.commit()
        return {"message": "Wemeje konti", "user_id": user.id}
    return {"error": "OTP ntabwo ihuye"}
