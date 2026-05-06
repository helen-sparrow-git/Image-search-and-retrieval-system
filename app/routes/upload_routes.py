from fastapi import APIRouter, UploadFile, File
from app.services.upload_service import process_upload
from app.schemas.upload_schema import UploadResponse

router = APIRouter()

@router.post("/upload", response_model=UploadResponse)
async def upload_file(file: UploadFile = File(...)):
    result = await process_upload(file)
    return result