from fastapi import APIRouter # type: ignore
from fastapi import Depends # type: ignore
from sqlalchemy.orm import Session # type: ignore
from backend.auth.jwt_handler import create_access_token

from backend.database.db import get_db
from backend.auth.auth import (
    register_user,
    authenticate_user
)

from backend.schemas.user_schema import (
    UserCreate,
    UserLogin
)

router = APIRouter()

@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    new_user = register_user(
        db,
        user.username,
        user.email,
        user.password
    )

    if not new_user:

        return {
            "message":
            "Username already exists"
        }

    return {
        "message":
        "Registration successful"
    }

@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    existing_user = authenticate_user(
        db,
        user.username,
        user.password
    )

    if not existing_user:

        return {
            "message":
            "Invalid credentials"
        }

    token = create_access_token(
        {
            "sub":
            existing_user.username
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }