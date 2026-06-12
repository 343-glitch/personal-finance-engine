from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, Float, String


class Base(DeclarativeBase):
    pass


class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)


class TransactionDB(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    user_email = Column(String)

    amount = Column(Float)
    category = Column(String)
    description = Column(String)
    date = Column(String)