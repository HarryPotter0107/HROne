import motor.motor_asyncio
from app.core.config import MONGO_URI, MONGO_DB

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB]
