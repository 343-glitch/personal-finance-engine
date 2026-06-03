from fastapi import APIRouter

from database import SessionLocal
from models import TransactionDB
from schemas.transaction import Transaction

router = APIRouter()


@router.post("/transactions")
def create_transaction(transaction: Transaction):
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
def get_transactions():
    db = SessionLocal()

    transactions = db.query(TransactionDB).all()

    return transactions