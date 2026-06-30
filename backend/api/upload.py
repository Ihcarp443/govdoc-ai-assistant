from fastapi import APIRouter, UploadFile, File, Form
from typing import List
import os
import shutil
import uuid

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_files(
    files: List[UploadFile] = File(...),
    thread_id: str = Form(...),
    user_id: str = Form(...)
):
    uploaded_paths = []

    for file in files:
        extension = os.path.splitext(file.filename)[1]

        filename = f"{uuid.uuid4()}{extension}"

        file_path = os.path.join(UPLOAD_DIR, filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        uploaded_paths.append(file_path)

    return {
        "success": True,
        "paths": uploaded_paths
    }