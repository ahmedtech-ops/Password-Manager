from models.password_model import Passwords
from db.db_init import database
from constants import password_collection
from utils.api_error import ApiError
from utils.api_response import ApiResponse
from dataclasses import asdict
import asyncio

async def createPassword(user_id,password_name,password_value):

    if  (user_id==None or user_id=="") and (password_name==None or password_name=="") and (password_value==None or password_value==""):
        return ApiError(400,"all fields are required")
    
    collection= database[password_collection]
    result=await collection.insert_one(asdict(Passwords(user_id,password_name,password_value)))
    return ApiResponse(200,"user created succesfully",result.inserted_id)



async def delPassword(user_id,password_name):
    if(user_id==None or user_id=="") and (password_name==None or password_name==""):
        return ApiError(400,"all field are required")
    
    collection= database[password_collection]
    passwordobject= asdict(Passwords(user_id,password_name,None))
    del passwordobject["password_value"]
    result=await collection.find_one_and_delete(passwordobject)

    if result==None:
        return ApiError(404,"password not found")
    return ApiResponse(200,"password deleted succesfully",result)

async def getpassword(user_id):
    if (user_id==None or user_id==""):
        return ApiError(400,"user id required")
    
    collection= database[password_collection]
    passwordobject= asdict(Passwords(user_id,None,None))
    del passwordobject["password_value"]
    del passwordobject["password_name"]
    result_cursor= collection.find(passwordobject)
    results=[]

    async for result in result_cursor:
        results.append(result)

    if not results:
        return ApiError(400,"not found")
    return ApiResponse(200,"found successully",result)



async def update(user_id,password_name,new_password):
    if (user_id==None or user_id=="") and (password_name==None or password_name=="") and (new_password==None or new_password==""):
        return ApiError(400,"user id required")
    
    collection= database[password_collection]
    passwordobject= asdict(Passwords(user_id,password_name))
    del passwordobject["password_value"]

    del passwordobject["password_value"]

    result=await collection.find_one_and_update(passwordobject,{"$set":{"password_value":new_password}})

    if result==None:
        return ApiError(404,"password not found")
    return ApiResponse(200,"password updated succesfully",result)







        


        
    