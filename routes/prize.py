from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_prize_breakdown():
    return {
        "jackpot": "30,000,000 RWF",
        "tiers": [
            {"match": "6 numbers", "prize": "30,000,000 RWF"},
            {"match": "5 numbers", "prize": "3,000,000 RWF"},
            {"match": "4 numbers", "prize": "1,000,000 RWF"},
            {"match": "3 numbers", "prize": "750,000 RWF"},
            {"match": "2 numbers", "prize": "250,000 RWF"},
        ],
        "odds": {
            "jackpot": "1 in 8,145,060",
            "any prize": "1 in 24"
        }
    }
