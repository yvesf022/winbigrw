from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models.ticket import Ticket
from config import TICKET_PRICE

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/user-room")
def user_room(user_id: int, db: Session = Depends(get_db)):
    tickets = db.query(Ticket).filter(Ticket.user_id == user_id).all()
    return {
        "tickets": [
            {
                "numbers": t.numbers,
                "is_winner": t.is_winner
            } for t in tickets
        ],
        "totalSpent": len(tickets) * TICKET_PRICE,
        "drawStatus": "Done" if any(t.is_winner for t in tickets) else "Pending"
    }
