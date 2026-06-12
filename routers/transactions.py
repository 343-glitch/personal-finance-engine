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
        date=transaction.date,
        user_email=current_user
    )

    db.add(new_transaction)
    db.commit()

    return {"message": "Transaction saved"}


@router.get("/transactions")
def get_transactions(
    current_user: str = Depends(get_current_user)
):
    db = SessionLocal()

    transactions = db.query(TransactionDB).filter(
        TransactionDB.user_email == current_user
    ).all()

    return transactions


@router.put("/transactions/{transaction_id}")
def update_transaction(
    transaction_id: int,
    updated_transaction: Transaction,
    current_user: str = Depends(get_current_user)
):
    db = SessionLocal()

    transaction = db.query(TransactionDB).filter(
        TransactionDB.id == transaction_id,
        TransactionDB.user_email == current_user
    ).first()

    if not transaction:
        return {"message": "Transaction not found"}

    transaction.amount = updated_transaction.amount
    transaction.category = updated_transaction.category
    transaction.description = updated_transaction.description
    transaction.date = updated_transaction.date

    db.commit()

    return {"message": "Transaction updated"}


@router.delete("/transactions/{transaction_id}")
def delete_transaction(
    transaction_id: int,
    current_user: str = Depends(get_current_user)
):
    db = SessionLocal()

    transaction = db.query(TransactionDB).filter(
        TransactionDB.id == transaction_id,
        TransactionDB.user_email == current_user
    ).first()

    if not transaction:
        return {"message": "Transaction not found"}

    db.delete(transaction)
    db.commit()

    return {"message": "Transaction deleted"}