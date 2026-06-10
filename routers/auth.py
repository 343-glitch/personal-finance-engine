from fastapi import APIRouter

from schemas.user import UserCreate
from schemas.login import UserLogin

from database import SessionLocal
from models import UserDB
from jwt_handler import create_access_token

from passlib.context import CryptContext

router = APIRouter()

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


@router.post("/register")
def register_user(user: UserCreate):
    db = SessionLocal()

    existing_user = db.query(UserDB).filter(
        UserDB.email == user.email
    ).first()

    if existing_user:
        return {
            "message": "Email already registered"
        }

    hashed_password = pwd_context.hash(user.password)

    new_user = UserDB(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()

    return {
        "message": "User registered successfully"
    }


@router.post("/login")
def login_user(user: UserLogin):
    db = SessionLocal()

    existing_user = db.query(UserDB).filter(
        UserDB.email == user.email
    ).first()

    if not existing_user:
        return {
            "message": "Invalid email or password"
        }

    if not pwd_context.verify(
        user.password,
        existing_user.password
    ):
        return {
            "message": "Invalid email or password"
        }

    token = create_access_token(
        {
            "sub": existing_user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }