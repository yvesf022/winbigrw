from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models.ticket import Ticket
from config import TOTAL_TICKETS, TICKET_PRICE

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/ticket")
def create_ticket(numbers: str, user_id: int, db: Session = Depends(get_db)):
    ticket = Ticket(numbers=numbers, user_id=user_id)
    db.add(ticket)
    db.commit()
    return {"message": "Itike yemejwe"}

@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    sold = db.query(Ticket).count()
    remaining = TOTAL_TICKETS - sold
    winners = db.query(Ticket).filter(Ticket.is_winner == True).count()
    return {
        "total": TOTAL_TICKETS,
        "sold": sold,
        "remaining": remaining,
        "winners": winners,
        "price": TICKET_PRICE
    }
