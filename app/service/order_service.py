from app.repository.order_repository import insert_order, find_orders_by_user, get_product_by_id

async def create_order_service(order):
    result = await insert_order(order.dict())
    return str(result.inserted_id)

async def get_orders_service(user_id: str, limit: int = 10, offset: int = 0):
    cursor = await find_orders_by_user(user_id, offset, limit)
    orders = []

    async for order in cursor:
        items = []
        total = 0.0
        for item in order["items"]:
            product = await get_product_by_id(item["productId"])
            if product:
                items.append({
                    "productDetails": {
                        "id": str(product["_id"]),
                        "name": product["name"]
                    },
                    "qty": item["qty"]
                })
                total += product["price"] * item["qty"]

        orders.append({
            "id": str(order["_id"]),
            "items": items,
            "total": round(total, 2)
        })

    return orders
