from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models.draw import Draw
from schemas import DrawCreate, DrawOut
from utils.session import get_current_admin
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=DrawOut)
def create_draw(draw: DrawCreate, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    # Convert list of integers to comma-separated string
    winning_str = ",".join(map(str, draw.winning_numbers))

    new_draw = Draw(
        date=draw.date,
        winning_numbers=winning_str
    )
    db.add(new_draw)
    db.commit()
    db.refresh(new_draw)

    return DrawOut(
        id=new_draw.id,
        date=new_draw.date,
        winning_numbers=draw.winning_numbers
    )

@router.get("/", response_model=list[DrawOut])
def list_draws(db: Session = Depends(get_db)):
    draws = db.query(Draw).order_by(Draw.date.desc()).all()

    return [
        DrawOut(
            id=d.id,
            date=d.date,
            winning_numbers=list(map(int, d.winning_numbers.split(",")))
        )
        for d in draws
    ]
