from fastapi import APIRouter
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os

from services.export_service import ExportService

router = APIRouter()

export_service = ExportService()


class ExportRequest(BaseModel):

    report: str

    file_type: str

    file_name: str | None = None


@router.post("/export")
def export_report(request: ExportRequest):

    filename = request.file_name

    if filename is None:

        filename = f"report.{request.file_type}"

    path = export_service.export(

        text=request.report,

        file_type=request.file_type,

        file_name=filename

    )

    media_types = {

        "pdf": "application/pdf",

        "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"

    }

    return FileResponse(

        path=path,

        filename=os.path.basename(path),

        media_type=media_types[request.file_type]

    )