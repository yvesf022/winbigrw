from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models.ticket import Ticket
from models.draw import Draw
from utils.session import get_current_user

router = APIRouter()

@router.post("/")
def validate_ticket(ticket_id: int, draw_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    ticket = db.query(Ticket).filter_by(id=ticket_id, user_id=user.id).first()
    draw = db.query(Draw).filter_by(id=draw_id).first()

    if not ticket or not draw:
        raise HTTPException(status_code=404, detail="Ticket or draw not found")

    ticket_numbers = list(map(int, ticket.numbers.split(",")))
    winning_numbers = list(map(int, draw.winning_numbers.split(",")))

    matched = set(ticket_numbers).intersection(set(winning_numbers))
    match_count = len(matched)

    prize_map = {
        6: "30,000,000 RWF",
        5: "3,000,000 RWF",
        4: "1,000,000 RWF",
        3: "750,000 RWF",
        2: "250,000 RWF"
    }

    prize = prize_map.get(match_count, "No prize")
    return {
        "matched_numbers": list(matched),
        "match_count": match_count,
        "prize": prize
    }
