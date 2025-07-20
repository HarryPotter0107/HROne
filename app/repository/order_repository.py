from app.database.mongodb import db

async def insert_order(order: dict):
    return await db.orders.insert_one(order)

async def find_orders_by_user(user_id: str, skip: int, limit: int):
    return db.orders.find({"userId": user_id}).skip(skip).limit(limit)

async def get_product_by_id(product_id):
    from bson import ObjectId
    return await db.products.find_one({"_id": ObjectId(product_id)})
