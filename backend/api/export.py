from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uuid
import os

from services.export_service import ExportService
from db_repo.doc_repository import save_document

router = APIRouter()

export_service = ExportService()


class ExportRequest(BaseModel):
    report: str
    file_type: str
    thread_id: str
    user_id: str
    file_name: str | None = None


@router.post("/export")
async def export_document(req: ExportRequest):
    try:

    GENERATED_DIR = "generated"

    filename = request.file_name or f"report.{request.file_type}"

    base_path = os.path.join(
        GENERATED_DIR,
        request.user_id,
        request.thread_id
    )

    os.makedirs(base_path, exist_ok=True)

    full_path = os.path.join(base_path, filename)

    path = export_service.export(
        markdown=request.report,
        file_type=request.file_type,
        file_name=full_path,
        path = full_path
    )

    media_types = {
        "pdf": "application/pdf",
        "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    }
    

    save_document(
        thread_id=request.thread_id,
        user_id=request.user_id,
        filename=os.path.basename(path),
        original_filename=filename,
        display_name=os.path.splitext(filename)[0],
        category="generated",
        file_type=request.file_type,
        file_path=path
    )

    return FileResponse(
        path=path,
        filename=os.path.basename(path),
        media_type=media_types[request.file_type]
    )
