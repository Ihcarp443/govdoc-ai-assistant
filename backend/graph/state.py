from typing import Annotated, List, Dict, Any
from langchain_core.messages import BaseMessage
from langgraph.graph.message import TypedDict, add_messages


class ChatMessage(TypedDict):
    role: str
    content: str
    answer_type: str

class GraphState(TypedDict, total=False):

    # Conversation
    messages: Annotated[List[BaseMessage], add_messages]
    chat_history: List[ChatMessage]

    # User Input
    user_id: str
    user_question: str
    input_type: str
    channel: str

    # Uploaded Files
    paths: List[str]

    # Processed Documents
    docs: List[Dict[str, Any]]
    # Routing
    intent: str

    # Final Response
    answer_en: str
    answer_type: str

# from typing import Annotated, Any, Dict, List, Optional
# from langchain_core.messages import BaseMessage
# from langgraph.graph.message import TypedDict, add_messages
# from typing import Annotated, List, Dict, Any
# from langchain_core.messages import BaseMessage
# from langgraph.graph.message import TypedDict, add_messages

# class ChatMessage(TypedDict):
#     role: str
#     content: str
#     answer_type: str

# class GraphState(TypedDict, total=False):
#     messages: Annotated[List[BaseMessage], add_messages]
#     chat_history: List[ChatMessage]
#     paths: List[str]
#     documents: List[str]
#     answer_en: str
#     intent:str
#     # final_answer: str
#     query_en: str
#     docs: list

#     # user_id: str
#     # memory: dict
#     # input_text: str
#     # input_type: str
#     # expanded_query:str
#     # channel:str
#     # user_lang: str
#     # filters: dict
#     # intent: str
#     # suggested_ques: List[str]
#     # feedback_mode: bool
#     # question: str
#     # original_answer: str
#     # feedback_reason: str
#     # feedback_comment: str
# # class GraphState(TypedDict, total=False):

# #     # Conversation
# #     messages: Annotated[List[BaseMessage], add_messages]
# #     chat_history: List[ChatMessage]

# #     # User Input
# #     user_id: str
# #     user_question: str
# #     input_type: str
# #     channel: str

# #     # Uploaded Files
# #     paths: List[str]

# #     # Processed Documents
# #     documents: List[Dict[str, Any]]

# #     # Routing
# #     intent: str

# #     # Final Response
# #     answer_en: str