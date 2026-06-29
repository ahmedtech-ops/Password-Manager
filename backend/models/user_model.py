from ..constants import  user_collection
from dataclasses import dataclass
from ..db.db_init import database



@dataclass
class User:
    name: str
    email: str
    password: str


async def create_user_collection():
    try:
        await database.create_collection(user_collection)
        print("user collection created")
    except Exception as e:
        raise Exception(f"failed to create user collections {e}")