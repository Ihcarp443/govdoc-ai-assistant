from fastapi import APIRouter, UploadFile, File, Form
from typing import List
import os
import shutil
from db_repo.doc_repository import save_document

router = APIRouter()


UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
import os

print("Current Working Directory:", os.getcwd())
print("UPLOAD_DIR:", os.path.abspath(UPLOAD_DIR))

@router.post("/upload")
async def upload_files(
    files: List[UploadFile] = File(...),
    thread_id: str = Form(...),
    user_id: str = Form(...),
    filenames: List[str] = Form(...)
):
    uploaded_paths = []
    if thread_id is None:
        thread_id = str(uuid.uuid4())
        save_thread(
            thread_id,
            user_id=req.user_id or '1234',
            title=req.message[:50],
        )
    else:
        thread_id = thread_id
        user_id = '2345'
    print('Uploading')
    # base path: uploads/user_id/thread_id

    base_path = os.path.join(UPLOAD_DIR, user_id, thread_id)
    os.makedirs(base_path, exist_ok=True)
    for file, frontend_name in zip(files, filenames):

        safe_name = os.path.basename(frontend_name)

        file_path = os.path.join(base_path, safe_name)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        uploaded_paths.append(file_path)

        save_document(
            thread_id=thread_id,
            user_id=user_id,
            filename=safe_name,
            original_filename=frontend_name,
            display_name=frontend_name,
            category="uploaded",
            file_type=os.path.splitext(safe_name)[1].lstrip("."),
            file_path=file_path
        )

    # for file, frontend_name in zip(files, filenames):
    #     # sanitize filename if needed
    #     safe_name = os.path.basename(frontend_name)

    #     file_path = os.path.join(base_path, safe_name)

    #     with open(file_path, "wb") as buffer:
    #         shutil.copyfileobj(file.file, buffer)

    #     uploaded_paths.append(file_path)

    return {
        "success": True,
        "paths": uploaded_paths
    }


# from fastapi import APIRouter, UploadFile, File, Form
# from typing import List
# import os
# import shutil
# import uuid

# router = APIRouter()

# UPLOAD_DIR = "uploads"

# os.makedirs(UPLOAD_DIR, exist_ok=True)


# @router.post("/upload")
# async def upload_files(
#     files: List[UploadFile] = File(...),
#     thread_id: str = Form(...),
#     user_id: str = Form(...)
# ):
#     uploaded_paths = []

#     for file in files:
#         extension = os.path.splitext(file.filename)[1]

#         filename = f"{uuid.uuid4()}{extension}"

#         file_path = os.path.join(UPLOAD_DIR, filename)

#         with open(file_path, "wb") as buffer:
#             shutil.copyfileobj(file.file, buffer)

#         uploaded_paths.append(file_path)

#     return {
#         "success": True,
#         "paths": uploaded_paths
#     }