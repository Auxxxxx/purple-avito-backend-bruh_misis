from pydantic import BaseModel
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from db.db import Base


class MicrocategoryBase(BaseModel):
    name: str
    parent_id: int


class MicrocategoryCreate(MicrocategoryBase):
    id: int 


class Microcategory(MicrocategoryCreate):

    class Config:
        from_attributes = True


class SqlMicrocategory(Base):
    __tablename__ = "microcategory"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    parent_id: Mapped[int] = mapped_column(Integer)
