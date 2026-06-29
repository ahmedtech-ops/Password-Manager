from ..constants import  password_collection
from dataclasses import dataclass
from ..db.db_init import database
import asyncio


@dataclass
class Passwords:
    user_id: str
    password_name: str
    password_value: str

async def create_password_collection():
    try:
        await database.create_collection(password_collection)
        print("password collection created")
    except Exception as e:
        raise Exception(f"failed to create password collections {e}")

asyncio.run(create_password_collection())

