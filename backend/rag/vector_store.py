
import os
import faiss
import pickle
import numpy as np


class FAISSStore:

    def __init__(self, dimension, user_id):

        self.dimension = dimension
        self.user_id = str(user_id)

        self.folder = os.path.join("DB", self.user_id)
        self.index_path = os.path.join(self.folder, "faiss.index")
        self.metadata_path = os.path.join(self.folder, "metadata.pkl")

        os.makedirs(self.folder, exist_ok=True)

        if os.path.exists(self.index_path):

            self.index = faiss.read_index(self.index_path)

            with open(self.metadata_path, "rb") as f:
                self.metadata = pickle.load(f)

        else:

            self.index = faiss.IndexFlatIP(dimension)
            self.metadata = []

    def add_documents(self, embeddings, chunks):

        embeddings = np.asarray(
            embeddings,
            dtype=np.float32
        )

        self.index.add(embeddings)

        self.metadata.extend(chunks)

    def save(self):

        faiss.write_index(
            self.index,
            self.index_path
        )

        with open(self.metadata_path, "wb") as f:
            pickle.dump(self.metadata, f)

    def search(self, query_embedding, k=5):

        scores, indices = self.index.search(
            query_embedding,
            k
        )

        results = []

        for score, idx in zip(scores[0], indices[0]):

            if idx == -1:
                continue

            results.append({
                "score": float(score),
                **self.metadata[idx]
            })

        return results