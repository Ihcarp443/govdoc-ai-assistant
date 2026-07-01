from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import uuid
import traceback
from graph.graph_builder import graph
from db_repo.thread_repository import save_thread
from langchain_core.messages import HumanMessage,AIMessage
# , update_thread_title
# from services.title_generator import generate_title
router = APIRouter()

print("Chat triggered successfully")

class ChatRequest(BaseModel):
    message: str
    thread_id: str | None = None
    input_type: str
    user_id: str | None = None
    paths: list[str] = []

@router.post("/chat")
async def chat(req: ChatRequest):
    print("req",req)
    if req.thread_id is None:
        thread_id = str(uuid.uuid4())
        save_thread(
            thread_id,
            user_id=req.user_id or '1234',
            title=req.message[:50],
        )
    else:
        thread_id = req.thread_id

    user_id=req.user_id
    print("user_id",user_id)
    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    state = {
        "user_id": user_id,
        "user_question": req.message,
        "channel": "website",
        "messages": [
            HumanMessage(content=req.message)
        ],
        "paths": req.paths,
        "answer_type": "text"
    }

    try:
        result = graph.invoke(
            state,
            config=config
        )
        # uncomment for title genration
        # title = generate_title(
        #     question=req.message,
        #     answer=result["answer_en"]
        # )

        # update_thread_title(
        #     thread_id,
        #     user_id,
        #     title
        # )

        return {
            "success": True,
            "thread_id": thread_id,
            "answer": result.get("answer_en", ""),
            "answer_type": result.get("answer_type", ""),
        }
    
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail="Something went wrong. Please try again."
        )

