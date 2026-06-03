# Personal Finance Intelligence Engine

A backend-driven personal finance analytics application built using FastAPI, SQLAlchemy, and SQLite.

## Features

* Create and store financial transactions
* Track amount, category, description, and date
* View all transactions
* Calculate total spending
* Analyze spending by category
* Generate spending insights
* Monthly spending analytics
* REST API with interactive Swagger documentation

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn

## API Endpoints

### Transactions

* POST /transactions
* GET /transactions

### Analytics

* GET /analytics/total
* GET /analytics/categories
* GET /analytics/insights
* GET /analytics/monthly

## Example Transaction

```json
{
  "amount": 1200,
  "category": "Shopping",
  "description": "Amazon",
  "date": "2026-06-03"
}
```

## Running Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Future Improvements

* Merchant analytics
* Budget tracking
* AI-powered spending insights
* Interactive dashboard
* Cloud deployment

## Author

Built as a portfolio project to demonstrate backend development, database design, REST APIs, and analytics using Python.
