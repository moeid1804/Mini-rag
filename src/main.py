from fastapi import FastAPI
from routes import base, data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings
app = FastAPI()
@app.on_event("startup")
async def startup_db_client():
    settings = get_settings()   
    app.mongodb_connect = AsyncIOMotorClient(settings.mongo_url)
    app.db_client = app.mongodb_connect[settings.mongodb_name]
@app.on_event("shutdown")
async def shutdown_db_client():
    await app.mongodb_connect.close()

app.include_router(base.base_router)
app.include_router(data.data_router)