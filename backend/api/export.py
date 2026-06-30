from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uuid
import os

from services.export_service import ExportService

router = APIRouter()

export_service = ExportService()


class ExportRequest(BaseModel):
    markdown: str
    file_type: str
    file_name: str | None = None


@router.post("/export")
async def export_document(req: ExportRequest):
    try:

        extension = req.file_type.lower()

        if extension not in ["pdf", "docx"]:
            raise HTTPException(
                status_code=400,
                detail="Invalid file type"
            )

        filename = req.file_name or f"{uuid.uuid4()}.{extension}"

        if not filename.endswith(f".{extension}"):
            filename += f".{extension}"

        file_path = export_service.export(
            markdown=req.markdown,
            file_type=extension,
            file_name=filename
        )

        return FileResponse(
            path=file_path,
            filename=filename,
            media_type="application/octet-stream"
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )