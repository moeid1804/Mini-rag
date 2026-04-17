from fastapi import FastAPI
from fastapi import APIRouter
import os

router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)


@router.get("/")
async def welcome():
    api_name = os.getenv("API_NAME")
    api_version = os.getenv("API_VERSION")
    return {
        "api_name ": api_name,
        "api_version ": api_version,
    }
