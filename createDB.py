from db_config import start_db_client
from tortoise import Tortoise,run_async
async def main():
    await start_db_client()
    await Tortoise.generate_schemas()

if __name__=='__main___':
    run_async(main())