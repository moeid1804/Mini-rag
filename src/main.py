from fastapi import FastAPI
from routes import base , data
from dotenv import load_dotenv

load_dotenv('.env')
app=FastAPI()
app.include_router(base.router)
app.include_router(data.data_router)