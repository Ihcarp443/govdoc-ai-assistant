# rag/faiss_store.py

import faiss
import pickle
import numpy as np


class FAISSStore:

    def __init__(self, dimension):

        self.index = faiss.IndexFlatIP(
            dimension
        )

        self.metadata = []

    def add_documents(
        self,
        embeddings,
        chunks
    ):

        embeddings = np.array(
            embeddings,
            dtype=np.float32
        )

        self.index.add(
            embeddings
        )

        self.metadata.extend(
            chunks
        )

    def save(self):

        faiss.write_index(
            self.index,
            "DB/faiss.index"
        )

        with open(
            "DB/metadata.pkl",
            "wb"
        ) as f:

            pickle.dump(
                self.metadata,
                f
            )

    @classmethod
    def load(cls):

        index = faiss.read_index(
            "DB/faiss.index"
        )

        with open(
            "DB/metadata.pkl",
            "rb"
        ) as f:

            metadata = pickle.load(f)

        store = cls(
            index.d
        )

        store.index = index
        store.metadata = metadata

        return store
    
    def search(self,query_embedding,k=5):

        scores, indices = (
            self.index.search(
                query_embedding,
                k
            )
        )

        results = []

        for idx in indices[0]:

            results.append(
                self.metadata[idx]
            )

        return results
    

