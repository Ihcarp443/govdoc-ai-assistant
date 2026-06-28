from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import uuid
import traceback
from graph.graph_builder import graph

router = APIRouter()

print("Chat triggered successfully")

class ChatRequest(BaseModel):
    message: str
    thread_id: str | None = None
    input_type: str
    user_id: str
    paths: list[str] = []

@router.post("/chat")
async def chat(req: ChatRequest):
    print(req)
    if req.thread_id is None:
        thread_id = req.thread_id or str(uuid.uuid4())
    else:
        thread_id = req.thread_id
    
    user_id=req.user_id or '1234'
    print("user_id",user_id)
    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }
    # state = {
    #     # "input_type": "text",
    #     "user_id":user_id,
    #     "ques_en":req.message,
    #     # "input_type": req.input_type,
    #     "input_text": req.message,
    #     "channel":"website",
    #     "messages": [],
    #     "paths": req.paths
    # }
    state = {
        "user_id": user_id,
        "user_question": req.message,
        # "input_type": req.input_type,
        "channel": "website",
        "messages": [],
        "paths": req.paths
    }

    try:
        result = graph.invoke(
            state,
            config=config
        )

        return {
            "success": True,
            "thread_id": thread_id,
            "answer": result.get("answer_en", "")
        }
    
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail="Something went wrong. Please try again."
        )

