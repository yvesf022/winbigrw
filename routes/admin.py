from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models.ticket import Ticket
import random

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/simulate-draw")
def simulate_draw(db: Session = Depends(get_db)):
    tickets = db.query(Ticket).all()
    if not tickets:
        return {"message": "Nta tike zihari"}

    winners = random.sample(tickets, min(5, len(tickets)))
    for ticket in winners:
        ticket.is_winner = True
    db.commit()

    return {
        "message": "Tombola yateguwe",
        "winners": [t.id for t in winners]
    }

@router.get("/export")
def export_tickets(db: Session = Depends(get_db)):
    tickets = db.query(Ticket).all()
    return {
        "tickets": [
            {"id": t.id, "numbers": t.numbers, "user_id": t.user_id, "is_winner": t.is_winner}
            for t in tickets
        ]
    }
