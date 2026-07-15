from models.user_model import User
from db.db_init import database
from constants import user_collection
from utils.api_error import ApiError
from utils.api_response import ApiResponse
from dataclasses import asdict
import asyncio

async def register(name :str, email:str, password:str):
    if (name==None or name=="") and (email==None or email=="") and (password==None or password==""):
        return ApiError(400,"all fields are required")
    
    collection= database[user_collection]
    result=await collection.insert_one(asdict(User(name,email,password)))
    return ApiResponse(200,"user created succesfully",result.inserted_id)




async def login(email,password):
    if (email==None or email=="") and (password==None or password==""):
    
        return ApiError(400,"all fields are required")
    
    collection=database[user_collection]
    user_data=asdict(User(None,email,password))
    del user_data["name"]
    result=await collection.find_one(user_data)
    if result==None:
       return ApiError(404,"user not found")
    return ApiResponse(200,"login succesfully",result)
print(asyncio.run(login("ahmed2332","ahmed112")))


    