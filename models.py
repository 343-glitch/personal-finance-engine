from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, Float, String


class Base(DeclarativeBase):
    pass


class TransactionDB(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    category = Column(String)
    description = Column(String)
    date = Column(String)