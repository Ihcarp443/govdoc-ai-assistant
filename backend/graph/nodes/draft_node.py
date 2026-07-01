from graph.state import GraphState
from services.drafting_service import DraftingService
from db_repo.thread_repository import add_chat_message
from langchain_core.messages import AIMessage

def draft_node(state: GraphState):
    extracted_docs = state.get("docs", [])
    user_id = state.get("user_id")
    thread_id = state.get("thread_id")
    user_question = state.get('user_question',"")
    drafter = DraftingService(user_id,thread_id)
    draft_response = drafter.generate(user_question, extracted_docs)
    print("Type of draft_response:", type(draft_response))
    return {
        "answer_en" : draft_response,
        "answer_type":"document",
        "messages": [
            AIMessage(content=draft_response)
        ],
        "chat_history":add_chat_message(state, "assistant", draft_response,"document")
    }