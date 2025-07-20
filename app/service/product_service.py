from app.repository.product_repository import insert_product, find_products

async def create_product_service(product):
    result = await insert_product(product.dict())
    return str(result.inserted_id)

async def list_products_service(name=None, size=None, limit=10, offset=0):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["sizes.size"] = size

    cursor = await find_products(query, offset, limit)
    products = []
    async for product in cursor:
        products.append({
            "id": str(product["_id"]),
            "name": product["name"],
            "price": product["price"]
        })
    return products
