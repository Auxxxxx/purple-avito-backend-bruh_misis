from sqlalchemy import update, delete
from sqlalchemy.orm import Session

from ..models.item import *


def create_item(db: Session, item: ItemCreate) -> SqlItem:
    db_item = SqlItem(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(db: Session, item: Item):
    update_query = update(SqlItem).where(SqlItem.id == item.id).values(item)
    db.execute(update_query)
    db.commit()


def get_item_by_id(db: Session, item_id: int) -> SqlItem:
    return db.query(SqlItem.id == item_id).one_or_none()


def delete_item_by_id(db: Session, item_id: int):
    db.execute(delete(SqlItem).where(SqlItem.id == item_id))
