from fastapi.responses import FileResponse
from fastapi import APIRouter

router = APIRouter()

@router.get("/documents/download")
async def download_document(file_path: str):
    return FileResponse(
        path=file_path,
        filename=file_path.split("\\")[-1],
        media_type="application/pdf"
    )