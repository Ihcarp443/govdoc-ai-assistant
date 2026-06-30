from fastapi import APIRouter, HTTPException
from db_repo.doc_repository import get_documents

router = APIRouter()

@router.get("/documents")
async def fetch_documents(
    thread_id: str,
    user_id: str
):
    try:
        documents = get_documents(
            thread_id=thread_id,
            user_id=user_id
        )

        return {
            "success": True,
            "documents": documents
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )