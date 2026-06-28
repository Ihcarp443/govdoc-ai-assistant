from rag.chunking import(ChunkingService)
from rag.embeddings import(EmbeddingService)
from rag.vector_store import(FAISSStore)
from providers.llm.hf_provider import HfProvider
from services.document_ingestion import (
    DocumentIngestionService
)

service = DocumentIngestionService()

result = service.process_pdf("notice.pdf")

document = result

chunking_service = ChunkingService()


chunks = chunking_service.create_chunks(document)

#======================================================== RETRIEVAL=====================================================

from rag.retrieval import Retriever
retriever = Retriever(user_id="103")
while True:
    user_question = input("\nAsk a question (or type 'exit' to quit): ")
    if user_question.lower() == "exit":
        break

    results = retriever.retrieve(
        user_question,
        top_k=5
    )

    context = "\n\n".join(
        chunk["text"]
        for chunk in results
    )
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

    hf_provider = HfProvider()
    response = hf_provider.generate(prompt)
    print(response.content)
