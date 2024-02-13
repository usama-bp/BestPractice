from pydantic import BaseModel




class CreateUser(BaseModel):
    name:str
    password:str



    class config:
        orm_mode=True
