from graph.state import GraphState
from services.drafting_service import DraftingService

def draft_node(state: GraphState):
    extracted_docs = state.get("docs", [])
    user_id = state.get("user_id")
    user_question = state.get('user_question',"")
    drafter = DraftingService(user_id)
    draft_response = drafter.generate(user_question, extracted_docs)
    return {
        "answer_en" : draft_response,
        "answer_type":"document"
    }