from sentence_transformers import SentenceTransformer, CrossEncoder
from rag.vector_store import FAISSStore
from rag.document_store import DocumentStore

class Retriever:

    def __init__(self, user_id):
        self.user_id = user_id

        self.embedding_model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

        self.reranker = CrossEncoder(
            "BAAI/bge-reranker-base"
        )
        self.document_store = DocumentStore(
            user_id=user_id
        )

        dimension = self.embedding_model.get_sentence_embedding_dimension()

        self.store = FAISSStore(
            dimension=dimension,
            user_id=user_id
        )

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        score_threshold: float = 0.55
    ):

        query_embedding = self.embedding_model.encode(
            [query],
            normalize_embeddings=True
        )

        scores, indices = self.store.index.search(
            query_embedding,
            top_k * 4
        )

        retrieved_chunks = []
        seen_chunks = set()

        # -------------------------------
        # Collect retrieved chunks
        # -------------------------------
        for score, idx in zip(scores[0], indices[0]):

            if idx == -1:
                continue

            if score < score_threshold:
                continue

            chunk = self.store.metadata[idx]

            unique_key = (
                chunk["document_id"],
                chunk["chunk_index"]
            )

            if unique_key in seen_chunks:
                continue

            seen_chunks.add(unique_key)

            chunk["faiss_score"] = float(score)

            retrieved_chunks.append(chunk)

        # Nothing found
        if not retrieved_chunks:
            return []

        # -------------------------------
        # Cross Encoder Reranking
        # -------------------------------
        pairs = [
            [query, chunk["text"]]
            for chunk in retrieved_chunks
        ]

        rerank_scores = self.reranker.predict(pairs)

        ranked = sorted(
            zip(rerank_scores, retrieved_chunks),
            key=lambda x: x[0],
            reverse=True
        )

        ranked = ranked[:top_k]

        results = []

        for rerank_score, chunk in ranked:

            results.append({

                "user_id": self.user_id or None,

                "score": round(float(rerank_score), 4),

                "faiss_score": round(chunk["faiss_score"], 4),

                "document_id": chunk["document_id"],

                "filename": chunk["filename"],

                "document_type": chunk["document_type"],

                "pages": chunk["pages"],

                "sources": chunk["sources"],

                "chunk_index": chunk["chunk_index"],

                "word_count": chunk["word_count"],

                "char_count": chunk["char_count"],

                "text": chunk["text"]

            })

        # -------------------------------
        # Debug Print
        # -------------------------------
        print("\n================ RETRIEVAL RESULTS ================\n")

        for i, result in enumerate(results, start=1):

            print(f"[{i}] CrossEncoder : {result['score']:.4f}")
            print(f"    FAISS Score : {result['faiss_score']:.4f}")
            print(f"    File        : {result['filename']}")
            print(f"    Type        : {result['document_type']}")
            print(f"    Pages       : {result['pages']}")
            print(f"    Sources     : {', '.join(result['sources'])}")
            print(f"    Chunk Index : {result['chunk_index']}")
            print(f"    Words       : {result['word_count']}")

            preview = result["text"].replace("\n", " ")

            if len(preview) > 350:
                preview = preview[:350] + "..."

            print()
            print(preview)
            print("\n--------------------------------------------------\n")

        return results
    
    def retrieve_documents(
        self,
        query: str,
        top_k: int = 3
    ):

        chunks = self.retrieve(
            query=query,
            top_k=top_k * 3
        )

        if not chunks:
            return []

        grouped = {}

        for chunk in chunks:

            doc_id = chunk["document_id"]

            if doc_id not in grouped:
                grouped[doc_id] = []

            grouped[doc_id].append(chunk)

        documents = []

        for doc_id, doc_chunks in grouped.items():

            document = self.document_store.get_document(doc_id)

            if not document:
                continue

            document = document.copy()
            document["chunks"] = doc_chunks

            documents.append(document)

        return documents
