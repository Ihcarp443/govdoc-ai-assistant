from services.document_ingestion import DocumentIngestionService
from graph.state import GraphState
from rag.document_store import DocumentStore

def extract_document(paths):
    service = DocumentIngestionService()
    results = []
    for path in paths:
        result = service.process_pdf(path)
        results.append(result)
    print("Results",results)
    return results
    # return service.process_pdf(path)

from rag.chunking import ChunkingService
from rag.embeddings import EmbeddingService
from rag.vector_store import FAISSStore


def store_documents(documents, user_id):

    if not documents:
        return

    chunker = ChunkingService()
    embedder = EmbeddingService()

    vector_store = FAISSStore(
        dimension=embedder.dimension,
        user_id=user_id
    )

    document_store = DocumentStore(
        user_id=user_id
    )

    chunks = []

    for document in documents:
        chunks.extend(
            chunker.create_chunks(document)
        )

    embeddings = embedder.create_embeddings(chunks)

    vector_store.add_documents(
        embeddings,
        chunks
    )

    vector_store.save()

    document_store.add_documents(documents)
    document_store.save()

    print(f"Stored {len(chunks)} chunks.")
    print(f"Stored {len(documents)} documents.")


def extractor(state: GraphState):
    paths = state["paths"]
    user_id = state["user_id"]

    extracted_docs = extract_document(paths)

    if extracted_docs:
        store_documents(
            extracted_docs,
            user_id
        )

    return {
        "docs": extracted_docs
    }