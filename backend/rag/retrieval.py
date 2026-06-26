from sentence_transformers import SentenceTransformer
from rag.vector_store import FAISSStore


class Retriever:

    def __init__(self):

        self.embedding_model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

        self.store = FAISSStore.load()

    def retrieve(self,query: str,top_k: int = 5):

        query_embedding = self.embedding_model.encode(
            [query],
            normalize_embeddings=True
        )

        scores, indices = self.store.index.search(
            query_embedding,
            top_k
        )

        results = []

        for score, idx in zip(
            scores[0],
            indices[0]
        ):

            if idx == -1:
                continue

            chunk = self.store.metadata[idx]

            results.append({
                "score": float(score),

                "document_id":
                    chunk["document_id"],

                "filename":
                    chunk["filename"],

                "document_type":
                    chunk["document_type"],

                "page":
                    chunk["page"],

                "source":
                    chunk["source"],

                "chunk_index":
                    chunk["chunk_index"],

                "text":
                    chunk["text"]
            })

        return results
    
