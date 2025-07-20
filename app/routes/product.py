from fastapi import APIRouter
from app.models.product_model import ProductModel, ProductResponseModel
from app.service.product_service import create_product_service, list_products_service

router = APIRouter()

@router.post("", response_model=ProductResponseModel)
async def create_product(product: ProductModel):
    product_id = await create_product_service(product)
    return {"id": product_id}

@router.get("")
async def list_products(name: str = None, size: str = None, limit: int = 10, offset: int = 0):
    data = await list_products_service(name, size, limit, offset)
    return {
        "data": data,
        "page": {
            "next": offset + limit,
            "previous": offset - limit if offset - limit >= 0 else None,
            "limit": limit
        }
    }
