from sqlalchemy import update, delete
from sqlalchemy.orm import Session

from ..models.item import *
from ..models.location import LocationCreate, SqlLocation, Location


def create_location(db: Session, location: LocationCreate) -> SqlLocation:
    db_location = SqlLocation(**location.model_dump())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location


def update_location(db: Session, location: Location):
    update_query = update(SqlLocation).where(SqlLocation.id == location.id).values(location)
    db.execute(update_query)
    db.commit()


def get_location_by_id(db: Session, location_id: int) -> SqlLocation:
    return db.query(SqlLocation.id == location_id).one_or_none()


def delete_location_by_id(db: Session, location_id: int):
    db.execute(delete(SqlLocation).where(SqlLocation.id == location_id))
