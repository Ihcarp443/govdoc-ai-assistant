from fastapi import APIRouter, HTTPException
from db_repo.doc_repository import get_documents

router = APIRouter()

@router.get("/documents")
async def fetch_documents(
    user_id: str
):
    print("===== DOCUMENT ROUTE CALLED =====")
    try:
        print("Received user_id:", user_id)
        documents = get_documents(
            user_id=user_id
        )
        print("Documents:", documents)
        return {
            "success": True,
            "documents": documents
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

# @router.get("/documents/{user_id}")
# async def fetch_documents(user_id: str):
#     try:
#         documents = get_documents(user_id)

#         return {
#             "success": True,
#             "documents": documents
#         }

#     except Exception as e:
#         raise HTTPException(
#             status_code=500,
#             detail=str(e)
#         )