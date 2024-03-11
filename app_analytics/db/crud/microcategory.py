from sqlalchemy import update, delete
from sqlalchemy.orm import Session

from ..models.item import *
from ..models.microcategory import MicrocategoryCreate, SqlMicrocategory, Microcategory


def create_microcategory(db: Session, microcategory: MicrocategoryCreate) -> SqlMicrocategory:
    db_microcategory = SqlMicrocategory(**microcategory.model_dump())
    db.add(db_microcategory)
    db.commit()
    db.refresh(db_microcategory)
    return db_microcategory


def update_microcategory(db: Session, microcategory: Microcategory):
    update_query = update(SqlMicrocategory).where(SqlMicrocategory.id == microcategory.id).values(microcategory)
    db.execute(update_query)
    db.commit()


def get_microcategory_by_id(db: Session, microcategory_id: int) -> SqlMicrocategory:
    return db.query(SqlMicrocategory.id == microcategory_id).one_or_none()


def delete_microcategory_by_id(db: Session, microcategory_id: int):
    db.execute(delete(SqlMicrocategory).where(SqlMicrocategory.id == microcategory_id))
