from fastapi import APIRouter
from app.models.order_model import OrderModel, OrderResponseModel
from app.service.order_service import create_order_service, get_orders_service

router = APIRouter()

@router.post("", response_model=OrderResponseModel)
async def create_order(order: OrderModel):
    order_id = await create_order_service(order)
    return {"id": order_id}

@router.get("/{user_id}")
async def get_orders(user_id: str, limit: int = 10, offset: int = 0):
    orders = await get_orders_service(user_id, limit, offset)
    return {
        "data": orders,
        "page": {
            "next": offset + limit,
            "previous": offset - limit if offset - limit >= 0 else None,
            "limit": limit
        }
    }
