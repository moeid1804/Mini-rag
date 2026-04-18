from fastapi import FastAPI ,APIRouter, Depends
from helpers.config import get_settings, Settings
import os

router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)


@router.get("/")
async def welcome(settings: Settings = Depends(get_settings)):

    api_name = settings.API_NAME
    api_version = settings.API_VERSION
    return {
        "api_name ": api_name,
        "api_version ": api_version,
    }
