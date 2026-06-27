from services.document_ingestion import (
    DocumentIngestionService
)

from services.document_classifier import (
    DocumentClassifier
)

from providers.llm.gemini_provider import (
    GeminiProvider
)

ingestion = DocumentIngestionService()

document = ingestion.process_pdf(
    "./Testing Data/Policy 3 Government Guarantee Policy.pdf"
)

classifier = DocumentClassifier(
    GeminiProvider()
)

document_type = classifier.classify(
    document["pages"]
)

print("\nDocument Type:")
print(document_type) 