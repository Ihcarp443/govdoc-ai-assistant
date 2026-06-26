from services.document_ingestion import (
    DocumentIngestionService
)

service = DocumentIngestionService()

result = service.process_pdf("notice.pdf")

print(f"\nDocument ID : {result['document_id']}")
print(f"Filename    : {result['filename']}")
print(f"Total Pages : {len(result['pages'])}")
print(f"Document Type: {result['metadata']['document_type']}")
print(f"Structure   : {result['metadata']['structure']}")
for page in result["pages"]:

    print("\n--------------------------------")
    print(f"Page    : {page['page']}")
    print(f"Source  : {page['source']}")
    print(f"Words   : {len(page['text'].split())}")
    print("--------------------------------")

    print(page["text"][:300])