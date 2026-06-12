from fastapi import FastAPI, Depends

from routers.transactions import router as transaction_router
from routers.analytics import router as analytics_router
from routers.auth import router as auth_router

from database import engine, SessionLocal
from models import Base, TransactionDB

from dependencies import get_current_user

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(transaction_router)
app.include_router(analytics_router)
app.include_router(auth_router)


@app.get("/analytics/total")
def total_spending(
    current_user: str = Depends(get_current_user)
):
    db = SessionLocal()

    transactions = db.query(TransactionDB).filter(
        TransactionDB.user_email == current_user
    ).all()

    total = sum(transaction.amount for transaction in transactions)

    return {"total_spending": total}


@app.get("/analytics/categories")
def category_breakdown(
    current_user: str = Depends(get_current_user)
):
    db = SessionLocal()

    transactions = db.query(TransactionDB).filter(
        TransactionDB.user_email == current_user
    ).all()

    breakdown = {}

    for transaction in transactions:
        category = transaction.category

        if category not in breakdown:
            breakdown[category] = 0

        breakdown[category] += transaction.amount

    return breakdown


@app.get("/analytics/insights")
def insights(
    current_user: str = Depends(get_current_user)
):
    db = SessionLocal()

    transactions = db.query(TransactionDB).filter(
        TransactionDB.user_email == current_user
    ).all()

    breakdown = {}

    for transaction in transactions:
        category = transaction.category

        if category not in breakdown:
            breakdown[category] = 0

        breakdown[category] += transaction.amount

    total_spent = sum(
        transaction.amount for transaction in transactions
    )

    average_transaction = (
        total_spent / len(transactions)
        if transactions else 0
    )

    top_category = (
        max(breakdown, key=breakdown.get)
        if breakdown else "None"
    )

    return {
        "total_transactions": len(transactions),
        "total_spent": total_spent,
        "average_transaction": average_transaction,
        "top_category": top_category
    }


@app.get("/")
def home():
    return {"message": "Hello Finance Engine"}