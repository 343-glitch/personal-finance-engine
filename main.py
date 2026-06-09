from fastapi import FastAPI

from routers.transactions import router as transaction_router
from routers.analytics import router as analytics_router
from routers.auth import router as auth_router

from database import engine, SessionLocal
from models import Base, TransactionDB

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(transaction_router)
app.include_router(analytics_router)
app.include_router(auth_router)


@app.get("/analytics/total")
def total_spending():
    db = SessionLocal()

    transactions = db.query(TransactionDB).all()

    total = sum(transaction.amount for transaction in transactions)

    return {"total_spending": total}


@app.get("/analytics/categories")
def category_breakdown():
    db = SessionLocal()

    transactions = db.query(TransactionDB).all()

    breakdown = {}

    for transaction in transactions:
        category = transaction.category

        if category not in breakdown:
            breakdown[category] = 0

        breakdown[category] += transaction.amount

    return breakdown


@app.get("/analytics/insights")
def insights():
    db = SessionLocal()

    transactions = db.query(TransactionDB).all()

    breakdown = {}

    for transaction in transactions:
        category = transaction.category

        if category not in breakdown:
            breakdown[category] = 0

        breakdown[category] += transaction.amount

    top_category = max(breakdown, key=breakdown.get)

    return {
        "total_transactions": len(transactions),
        "top_category": top_category
    }


@app.get("/")
def home():
    return {"message": "Hello Finance Engine"}