# db_config.py
from dotenv import load_dotenv
import os
from tortoise import Tortoise, fields,run_async
from settings import Settings

# username=str(os.getenv("USERNAME"))
# password=str(os.getenv("PASSWORD"))
# port=str(os.getenv("PORT"))
# host=str(os.getenv("HOST"))
# db_name=str(os.getenv("DATABASE_NAME"))

load_dotenv()

setting=Settings()
MODULES_LIST=["app.users.model"]


DB_URL=os.getenv("DB_URL")

# DB_CONFIG = {
#     # "database_url": username,
#     "username": username,
#     "password": password,
#     "host": host,
#     "port": port,  # Port number for PostgreSQL, change as needed
#     "database_name": db_name,
#     # Additional database-specific parameters can be added here
# }



async def start_db_client():

    # database_url=load_dotenv("DATABSE_URL")    
    await Tortoise.init(
        # db_url='sqlite://db.sqlite3',
        #  db_url=setting.database_url,
        db_url=DB_URL,
        modules={'models': MODULES_LIST}
    )
    await Tortoise.generate_schemas()

async def shutdown_db_client():
     await Tortoise.close_connections()
    



