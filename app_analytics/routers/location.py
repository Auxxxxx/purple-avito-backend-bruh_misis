from copy import copy
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from db.db import SessionLocal
from dependencies import is_admin, get_db
from db.models.item import Item, ItemCreate
from db.crud.item import create_item, get_item_by_id
from mock.mock_data import collect_json, get_locations_tree

router = APIRouter(
    prefix="/location",
    tags=["locations"],
    responses={404: {"description": "Not found"},
               500: {"description": "Internal server error"},
               403: {"description": "only admin user can create items"}},
)


@router.get("/")
async def get_root():
    try:
        root = get_locations_tree()
        for child in root.children:
            child.children = []
        location_json = collect_json(root)
    except Exception as e:
        print(e.__cause__)
        raise HTTPException(status_code=404, detail="Not found")
    return location_json


@router.get("/{node_id1}")
async def get_node1(node_id1: int):
    try:
        root = get_locations_tree()
        node1 = list(filter(lambda x: x.id == node_id1, root.children))[0]
        location_json = collect_json(node1)
    except Exception as e:
        print(e.__cause__)
        raise HTTPException(status_code=404, detail="Not found")
    return location_json


@router.get("/{node_id1}/{node_id2}")
async def get_node1(node_id1: int, node_id2: int):
    try:
        root = get_locations_tree()
        node1 = list(filter(lambda x: x.id == node_id1, root.children))[0]
        node2 = list(filter(lambda x: x.id == node_id2, node1.children))[0]
        location_json = collect_json(node2)
    except Exception as e:
        print(e.__cause__)
        raise HTTPException(status_code=404, detail="Not found")
    return location_json
