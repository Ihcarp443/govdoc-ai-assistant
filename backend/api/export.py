from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
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
    uploaded_file_name: str | None = None


@router.post("/export")
async def export_document(req: ExportRequest):
    try:
        print("req",req)
        GENERATED_DIR = "generated"

        filename = req.file_name or f"report.{req.file_type}"

        base_path = os.path.join(
            GENERATED_DIR,
            req.user_id,
            req.thread_id,
        )

        os.makedirs(base_path, exist_ok=True)

        full_path = os.path.join(base_path, filename)

        path = export_service.export(
            markdown=req.report,
            file_type=req.file_type,
            file_name=full_path,
            path=full_path,
        )

        media_types = {
            "pdf": "application/pdf",
            "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        }

        save_document(
            thread_id=req.thread_id,
            user_id=req.user_id,
            filename=os.path.basename(path),
            original_filename=filename,
            display_name=os.path.splitext(filename)[0],
            category="generated",
            file_type=req.file_type,
            file_path=path,
        )

        return FileResponse(
            path=path,
            filename=os.path.basename(path),
            media_type=media_types[req.file_type],
        )

    except Exception as e:
        print("Error occurred:", e)
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )