from fastapi import Depends
from pydantic import BaseModel
from sqlalchemy import Integer, String, event
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from mock.mock_data import get_locations_tree

from dependencies import get_db
from db.db import Base
from ..db import SessionLocal


class LocationBase(BaseModel):
    name: str
    parent_id: int


class LocationCreate(LocationBase):
    id: int

    def __init__(self, id: int, name: str, parent_id: int):
        super().__init__()
        self.id = id
        self.str = str
        self.parent_id = parent_id

class Location(LocationCreate):

    class Config:
        from_attributes = True


class SqlLocation(Base):
    __tablename__ = "location"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    parent_id: Mapped[int] = mapped_column(Integer)


@event.listens_for(SqlLocation.__table__, 'after_create')
def insert_initial_values(db: SessionLocal = Depends(get_db), *args, **kwargs):
    location = LocationCreate(1, "a", 5)
    db_location = SqlLocation(**location.model_dump())
    db.add(db_location)
    db.commit()