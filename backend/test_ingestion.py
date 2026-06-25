from services.document_ingestion import (
    DocumentIngestionService
)

service = DocumentIngestionService()

result = service.process_pdf(
    "test.pdf"
)

for page in result:

    print("\n===================")
    print("PAGE:", page["page"])
    print("SOURCE:", page["source"])
    print("===================")

    print(page["text"][:500])