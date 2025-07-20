from pydantic import BaseModel
from typing import List

class ItemModel(BaseModel):
    productId: str
    qty: int

class OrderModel(BaseModel):
    userId: str
    items: List[ItemModel]

class OrderResponseModel(BaseModel):
    id: str
