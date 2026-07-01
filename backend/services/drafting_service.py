from rag.retrieval import Retriever
# from services.llm_service import model\
from providers.llm.hf_provider import HfProvider


class DraftingService:

    def __init__(self,user_id,thread_id):
        self.retriever = Retriever(user_id,thread_id)

    def generate(self, query, user_docs=None):
        documents = self.retriever.retrieve_documents(
            query=query,
            top_k=10
        )
        if not documents:
            return "No similar documents were found."

        reference_documents = ""


        for i, document in enumerate(documents[:3], start=1):

            reference_documents += f"""
=========================
REFERENCE DOCUMENT {i}
=========================

Document Type:
{document["metadata"]["document_type"]}

Document Flow:
{", ".join(document["metadata"]["document_flow"])}

Structure:
"""

            for section in document["metadata"]["structure"]:

                reference_documents += (
                    f'- {section["heading"]}: '
                    f'{section.get("summary","")}\n'
                )

            reference_documents += "\nRelevant Content:\n\n"

            for chunk in document["chunks"][:3]:

                reference_documents += (
                    chunk["text"] + "\n\n"
                )

        prompt = f"""
You are an expert Government Document Drafting Assistant.

A user wants to draft a NEW document.

User Request:
{query}

You have been provided with similar documents retrieved from the knowledge base.

Use them ONLY as references for:

- writing style
- logical flow
- section ordering
- document structure
- formatting

Do NOT copy:

- names
- dates
- addresses
- tender numbers
- notification IDs
- monetary values
- phone numbers
- organization names

Generate a completely new document suitable for the user's request.

Reference Documents retrieved from the knowledge base:

{reference_documents}

Return only the drafted document.
"""
        model = HfProvider()
        response = model.generate(prompt)

        return response.content