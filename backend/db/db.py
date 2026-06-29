from dotenv import load_dotenv
import pymongo
from pymongo import AsyncMongoClient
import os
import asyncio
load_dotenv()

async def connect_db():
    try:
        result = AsyncMongoClient(
            os.getenv("MONGODB_URI"),
            server_api=pymongo.server_api.ServerApi(
                version="1",
                strict=True,
                deprecation_errors=True
            )
        )
        print("connected to db")
    except Exception as e:
        raise Exception(f"failed to connect to db {e}")