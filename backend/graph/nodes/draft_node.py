from graph.state import GraphState
from services.drafting_service import DraftingService

def draft_node(state: GraphState):
    # Extract necessary information from the state
    extracted_docs = state.get("docs", [])
    user_id = state.get("user_id")
    user_question = state.get('user_question',"")
    drafter = DraftingService(user_id)


    # Generate a draft response using a language model
    draft_response = drafter.generate(user_question, extracted_docs)

    # Update the state with the drafted response
    state["answer_en"] = draft_response

    return state