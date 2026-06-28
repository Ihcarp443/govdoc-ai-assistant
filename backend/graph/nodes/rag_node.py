from rag.chunking import ChunkingService
from rag.embeddings import EmbeddingService
from rag.vector_store import FAISSStore
from rag.retrieval import Retriever
from services.llm_service import model
from graph.state import GraphState

def rag_node(state: GraphState):
    documents = state["docs"]
    user_question = state["user_question"]
    user_id = state.get("user_id", "None") 
    # if documents:
    # # New document uploaded
    #     chunking_service = ChunkingService()

    #     chunks = []

    #     for document in documents:
    #         chunks.extend(
    #             chunking_service.create_chunks(document)
    #         )

    #     embedder = EmbeddingService()

    #     embeddings = embedder.create_embeddings(chunks)

    #     dimension = len(embeddings[0])

    #     store = FAISSStore(
    #         dimension=dimension,
    #         user_id=user_id
    #     )

    #     store.add_documents(
    #         embeddings,
    #         chunks
    #     )

    #     store.save()

    # print(f"Stored {len(chunks)} chunks")

    # 🔹 Retrieval
    retriever = Retriever(user_id=user_id)
    results = retriever.retrieve(user_question, top_k=3)

    context = "\n\n".join(chunk["text"] for chunk in results)

    # 🔹 Prompt
    prompt = f"""
    You are an AI assistant specialized in government documents.

    Instructions:
    - Answer ONLY from the provided context.
    - If the answer is not present, say:
      "I could not find this information in the document."
    - Do not make assumptions.
    - Rewrite OCR errors into proper readable language when possible.
    - Provide a concise answer.

    Context:
    {context}

    Question:
    {user_question}

    Answer:
    """

    # 🔹 LLM response
    response = model.invoke(prompt)
    return {
        'answer_en':response.content
    }
