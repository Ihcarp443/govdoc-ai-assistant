from graph.state import GraphState
from services.llm_service import model

prompt = """
You are an intent classifier for a Government Document Assistant.

Your job is to classify the user's request into ONE of the following intents.

1. rag
Use when the user is:
- asking questions about uploaded documents
- requesting information
- asking to summarize
- asking to explain
- asking to compare
- asking to extract information
- asking what a document contains

Examples:
"What is the eligibility criteria?"
"Summarize this notification."
"What is the estimated cost?"
"Who issued this circular?"
"Compare these two policies."

Return:
rag

-----------------------------------------

2. draft
Use when the user wants the AI to CREATE a NEW document.

Examples:
"Draft a tender for road maintenance."
"Generate a notice."
"Write a policy for widow pension."
"Create a government circular."
"Prepare an office memorandum."

Return:
draft

-----------------------------------------

Rules:
- Return ONLY one word.
- Output must be exactly:
rag
OR
draft

User Query:
{0}
"""

def intent_node(state: GraphState):

    user_question = state["user_question"]

    response = model.invoke(
        prompt.format(user_question)
    )

    state["intent"] = response.content.strip().lower()

    return state

def route(state):

    if state["intent"] == "draft":
        return "draft"

    return "rag"