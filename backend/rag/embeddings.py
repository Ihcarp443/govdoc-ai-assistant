from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(self):

        self.model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

    def create_embeddings(self, chunks):

        texts = [
            chunk["text"]
            for chunk in chunks
        ]

        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True,
            show_progress_bar=True
        )

        return embeddings