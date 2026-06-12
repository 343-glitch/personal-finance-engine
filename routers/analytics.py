from fastapi import APIRouter, Depends

from database import SessionLocal
from models import TransactionDB

from dependencies import get_current_user

router = APIRouter()


@router.get("/analytics/monthly")
def monthly_spending(
    current_user: str = Depends(get_current_user)
):
    db = SessionLocal()

    transactions = db.query(TransactionDB).filter(
        TransactionDB.user_email == current_user
    ).all()

    monthly_data = {}

    for transaction in transactions:
        month = transaction.date[:7]

        if month not in monthly_data:
            monthly_data[month] = 0

        monthly_data[month] += transaction.amount

    return monthly_data