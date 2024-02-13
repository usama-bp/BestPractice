from fastapi import FastAPI
from dotenv import load_dotenv
from tortoise.contrib.fastapi import register_tortoise
from app.users import routes as users_routes
# from db_config import DB_URL
from contextlib import asynccontextmanager
from db_config import start_db_client,shutdown_db_client
import os
from dotenv import load_dotenv
load_dotenv()
DB_URL=os.getenv("DB_URL")
from tortoise import Tortoise




MODULES_LIST=["app.users.model"]



asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    await start_db_client()

    yield
    # Clean up the ML models and release the resources
    await shutdown_db_client()








app=FastAPI(lifespan=lifespan)



# @app.get("/")
# async def home():
#     return {"message":"Home"}


app.include_router(users_routes.router)





Tortoise.init_models(MODULES_LIST,"models")


register_tortoise(
      app,
      db_url=DB_URL,
    modules={'models': MODULES_LIST},
        
    generate_schemas=True,
    add_exception_handlers=True,


)