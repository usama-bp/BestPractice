from tortoise import Tortoise, fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator






class Users(Model):
    id=fields.IntField(pk=True)
    name=fields.TextField()
    password=fields.TextField()
    created_at=fields.DatetimeField(auto_now_add=True)
    updated_at=fields.DatetimeField(auto_now=True)

    def __str__(self) :
        return self.name


UserModel=pydantic_model_creator(Users)

