from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from db.db import SessionLocal
from dependencies import is_admin, get_db
from db.models.item import Item, ItemCreate
from db.crud.item import create_item, get_item_by_id
from mock.mock_category import collect_json, get_category_tree

router = APIRouter(
    prefix="/category",
    tags=["category"],
    responses={404: {"description": "Not found"},
               500: {"description": "Internal server error"},
               403: {"description": "only admin user can create items"}},
)


@router.get("/")
async def get_root():
    try:
        root = get_category_tree()
        for child in root.children:
            child.children = []
        categorys_json = collect_json(root)
    except Exception as e:
        print(e.__cause__)
        raise HTTPException(status_code=404, detail="Not found")
    return categorys_json


@router.get("/{node_id1}")
async def get_node1(node_id1: int):
    try:
        root = get_category_tree()
        node1 = list(filter(lambda x: x.id == node_id1, root.children))[0]
        category_json = collect_json(node1)
    except Exception as e:
        print(e.__cause__)
        raise HTTPException(status_code=404, detail="Not found")
    return category_json


@router.get("/{node_id1}/{node_id2}")
async def get_node1(node_id1: int, node_id2: int):
    try:
        root = get_category_tree()
        node1 = list(filter(lambda x: x.id == node_id1, root.children))[0]
        node2 = list(filter(lambda x: x.id == node_id2, node1.children))[0]
        category_json = collect_json(node2)
    except Exception as e:
        print(e.__cause__)
        raise HTTPException(status_code=404, detail="Not found")
    return category_json
