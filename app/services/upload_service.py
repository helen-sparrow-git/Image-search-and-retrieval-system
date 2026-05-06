from fastapi import UploadFile
import os

UPLOAD_DIR = "uploads"

async def process_upload(file: UploadFile) -> dict:
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    return{
        "filename": file.filename,
        "content_type": file.content_type,
        "status": "uploaded"
    }