import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

def get_database():
    MONGO_URL = os.getenv("MONGODB")
    client = AsyncIOMotorClient(MONGO_URL)
    return client["homeMadeFood"]
