from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from routes import (
    user,
    auth,
    ticket,
    admin,
    draw,
    prize,
    validate
)

# Optional: create tables on startup (for dev only)
from db import Base, engine
from models import user as user_model, ticket as ticket_model, draw as draw_model

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Win Big Rwanda API",
    description="Backend for Win Big Rwanda lottery platform — secure, scalable, and culturally tailored",
    version="2.0.0"
)

# CORS setup for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check
@app.get("/")
def root():
    return {"message": "Win Big Rwanda backend is live and secure!"}

# Core user and ticket flows
app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(ticket.router, prefix="/ticket", tags=["Ticket"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])

# Powerball-style enhancements
app.include_router(draw.router, prefix="/draws", tags=["Draw History"])
app.include_router(prize.router, prefix="/prizes", tags=["Prize Breakdown"])
app.include_router(validate.router, prefix="/validate", tags=["Ticket Validation"])
