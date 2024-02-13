from pickle import EMPTY_LIST
from fastapi import Header,Request,HTTPException
from .model import Users
from typing import Optional







def get_token_info(*,token=Header(),request:Request):
        if token=="success":
            return True
        else:
            return False
             
    

async def get_all_users(token):
    if token is True:
        users=await Users.all()
        print(users)
        if users==False:
             return False
        else:
            return{"Users":users}


async def create_new_user(name:str,password:str):
    create_user=await Users.create(name=name,password=password)
    if create_user:
         return True
    else:
         return False
    
               