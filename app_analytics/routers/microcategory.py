from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from db.db import SessionLocal
from dependencies import is_admin, get_db
from db.models.item import Item, ItemCreate
from db.crud.item import create_item, get_item_by_id
from mock.mock_category import collect_json

router = APIRouter(
    prefix="/microcategory",
    tags=["microcategory"],
    responses={404: {"description": "Not found"},
               500: {"description": "Internal server error"},
               403: {"description": "only admin user can create items"}},
)


@router.get("/")
async def get_microcategories():
    microcategory_json = collect_json()

    return microcategory_json
