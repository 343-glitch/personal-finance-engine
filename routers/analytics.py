from fastapi import APIRouter

from database import SessionLocal
from models import TransactionDB

router = APIRouter()


@router.get("/analytics/monthly")
def monthly_spending():
    db = SessionLocal()

    transactions = db.query(TransactionDB).all()

    monthly_data = {}

    for transaction in transactions:
        month = transaction.date[:7]

        if month not in monthly_data:
            monthly_data[month] = 0

        monthly_data[month] += transaction.amount

    return monthly_data