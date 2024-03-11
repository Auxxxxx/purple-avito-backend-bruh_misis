from fastapi import Depends
from pydantic import BaseModel
from sqlalchemy import Integer, String, event
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from mock.mock_data import get_locations_tree

from dependencies import get_db
from .base import Base


class LocationBase(BaseModel):
    name: str
    parent_id: int


class LocationCreate(LocationBase):
    id: int


class Location(LocationCreate):

    class Config:
        from_attributes = True


class SqlLocation(Base):
    __tablename__ = "location"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    parent_id: Mapped[int] = mapped_column(Integer)


@event.listens_for(SqlLocation.__table__, 'after_create')
def insert_initial_values(*args, **kwargs):
    with Depends(get_db) as db:
        initial_locations = get_locations_tree()