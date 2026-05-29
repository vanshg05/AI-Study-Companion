from sqlalchemy import Column # type: ignore
from sqlalchemy import Integer # type: ignore
from sqlalchemy import String # type: ignore
from sqlalchemy import DateTime # type: ignore
from datetime import datetime

from backend.database.db import Base

class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String,
        unique=True,
        index=True
    )

    email = Column(
        String,
        unique=True,
        index=True
    )

    password = Column(
        String
    )

class Activity(Base):

    __tablename__ = "activities"

    id = Column(
        Integer,
        primary_key=True
    )

    username = Column(
        String
    )

    activity_type = Column(
        String
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )