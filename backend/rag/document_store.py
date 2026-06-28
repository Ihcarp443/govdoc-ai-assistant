import os
import pickle


class DocumentStore:

    def __init__(self, user_id):

        self.user_id = str(user_id)

        self.folder = os.path.join("DB", self.user_id)
        self.path = os.path.join(self.folder, "documents.pkl")

        os.makedirs(self.folder, exist_ok=True)

        if os.path.exists(self.path):
            with open(self.path, "rb") as f:
                self.documents = pickle.load(f)
        else:
            self.documents = {}

    def add_documents(self, documents):

        for document in documents:

            self.documents[document["document_id"]] = document

    def save(self):

        with open(self.path, "wb") as f:
            pickle.dump(self.documents, f)

    def get_document(self, document_id):

        return self.documents.get(document_id)

    def get_documents(self, document_ids):

        return [
            self.documents[id]
            for id in document_ids
            if id in self.documents
        ]