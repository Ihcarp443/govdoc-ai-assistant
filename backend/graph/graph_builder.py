from langgraph.graph import (StateGraph, START, END)
from langgraph.checkpoint.memory import MemorySaver
from graph.state import GraphState
from graph.nodes.extract_docs import extractor
from graph.nodes.rag_node import rag_node
from graph.nodes.intent_node import (intent_node, route)
from graph.nodes.draft_node import draft_node


builder = StateGraph(GraphState)



builder.add_node("extractor", extractor)
builder.add_node("intent", intent_node)
builder.add_node("rag", rag_node)
builder.add_node("draft", draft_node)

builder.add_edge(START, "extractor")
builder.add_edge("extractor", "intent")

builder.add_conditional_edges(
    "intent",
    route,
    {
        "rag": "rag",
        "draft": "draft"
    }
)

builder.add_edge("rag", END)
builder.add_edge("draft", END)
check = MemorySaver()
graph = builder.compile(checkpointer=check)
print('Graph compiled succesfully')