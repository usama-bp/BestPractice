from fastapi import APIRouter,Depends
from .model import Users
from .typers import CreateUser
from .controller import get_token_info,get_all_users,create_new_user
from typing import Optional



router=APIRouter(prefix="/users",tags=["users"],dependencies=[],responses={404:{"description":"Not Found"}})



@router.get("")
@router.get("/")
async def get_Users(token=Depends(get_token_info)):

    if token==False:
        return {"message":"Invalid Credientials"}
    else:
        users=await get_all_users(token)
        if users:
            return {"Users":users}
        else:
            return{"message":"Users Not Found"}

  

@router.post("/create_user")
async def create_user(user:CreateUser,token=Depends(get_token_info)):
    if token!=False:
        created_user=await create_new_user(user.name,user.password)
        if created_user:
            return {"message":"user created"}
        else:
            return {"message":"user not created"}
    else:
        return{"message":"Invalid Credientials"}