from fastapi import FastAPI, APIRouter, Depends, UploadFile
from helpers.config import get_settings, Settings
import os
from controllers import DataController, BaseController

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api/v1"],
)


@data_router.post("/upload")
async def upload_file(
    project_id: str, file: UploadFile, settings: Settings = Depends(get_settings)
):

    isvalid = DataController().validate_file(file=file)
    return isvalid
