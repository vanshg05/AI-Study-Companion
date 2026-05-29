from sqlalchemy.orm import Session # type: ignore

from backend.database.models import User
from backend.auth.hashing import (
    hash_password,
    verify_password
)

def register_user(
    db: Session,
    username: str,
    email: str,
    password: str
):

    existing_user = db.query(User).filter(
        User.username == username
    ).first()

    if existing_user:

        return None

    user = User(
        username=username,
        email=email,
        password=hash_password(password)
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user

def authenticate_user(
    db: Session,
    username: str,
    password: str
):

    user = db.query(User).filter(
        User.username == username
    ).first()

    if not user:

        return None

    if not verify_password(
        password,
        user.password
    ):

        return None

    return user