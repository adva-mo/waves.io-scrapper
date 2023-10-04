from typing import List
from datetime import datetime
from sqlalchemy import String, DateTime, Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


users_subscriptions = Table(
    "users_locations",
    Base.metadata,
    Column("user.id", ForeignKey("user.id"), primary_key=True),
    Column("location.id", ForeignKey("location.id"), primary_key=True),
)


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), unique=False, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), unique=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    phone: Mapped[str] = mapped_column(String(20), unique=True, nullable=True)
    locations: Mapped[List["Location"]] = relationship(
        back_populates="users", secondary="users_locations"
    )


class Location(Base):
    __tablename__ = "location"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name_he: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    name_en: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    users: Mapped[List["User"]] = relationship(
        back_populates="locations", secondary="users_locations"
    )

    def __str__(self):
        return self.name_he
