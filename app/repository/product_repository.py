from app.database.mongodb import db

async def insert_product(product: dict):
    return await db.products.insert_one(product)

async def find_products(query: dict, skip: int, limit: int):
    return db.products.find(query).skip(skip).limit(limit)
