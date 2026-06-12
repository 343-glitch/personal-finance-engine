from fastapi import APIRouter, Depends

from database import SessionLocal
from models import TransactionDB
from schemas.transaction import Transaction

from dependencies import get_current_user

router = APIRouter()


@router.post("/transactions")
def create_transaction(
    transaction: Transaction,
    current_user: str = Depends(get_current_user)
):
    db = SessionLocal()

    new_transaction = TransactionDB(
        amount=transaction.amount,
        category=transaction.category,
        description=transaction.description,
        date=transaction.date
    )

    db.add(new_transaction)
    db.commit()

    return {"message": "Transaction saved"}


@router.get("/transactions")
def get_transactions(
    current_user: str = Depends(get_current_user)
):
    db = SessionLocal()

    transactions = db.query(TransactionDB).all()

    return transactions