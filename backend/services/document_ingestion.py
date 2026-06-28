# D:\project2\backend\services\document_ingestion.py
import os
import uuid
from providers.pdf.pdf_extractor import PDFExtractor
from providers.ocr.easyocr_provider import EasyOCRProvider
from services.document_classifier import DocumentClassifier
from providers.llm.gemini_provider import GeminiProvider
from services.structure_extractor import StructureExtractor
from providers.layout.docling_provider import DoclingProvider
class DocumentIngestionService:

    def __init__(self):

        self.pdf_extractor = PDFExtractor()
        self.ocr_provider = EasyOCRProvider()

        self.document_classifier = DocumentClassifier(GeminiProvider())
        self.structure_extractor = StructureExtractor(GeminiProvider())
        self.layout_provider = DoclingProvider()

    def process_pdf(self, pdf_path):

        pages = self.pdf_extractor.split_pdf_pages(
            pdf_path,
            "backend/data/pages"
        )

        processed_pages = []

        for page in pages:

            extracted_text = page["text"]

            source = "pdf_text"

            if len(extracted_text.split()) < 20:

                extracted_text = self.ocr_provider.extract_text(
                    page["image_path"]
                )

                source = "ocr"

            processed_pages.append({
                "page": page["page"],
                "source": source,
                "image_path": page["image_path"],
                "word_count": len(extracted_text.split()),
                "text": extracted_text
            })

        document_type = self.document_classifier.classify(processed_pages)
        layout_markdown = self.layout_provider.extract_layout(pdf_path)
        print(f"\nLayout Markdown:\n{layout_markdown}\n")
        structure = self.structure_extractor.extract(processed_pages, layout_markdown)
        print(f"\nExtracted Structure:\n{structure}\n")
        
        # document_type = "unlabeled"
        return {
            "document_id": str(uuid.uuid4()),
            "filename": os.path.basename(pdf_path),

            "metadata": {

                "document_type": document_type,

                "structure": structure["sections"],

                "document_flow": [
                    section["heading"]
                    for section in structure["sections"]
                ],

                "section_count": len(structure["sections"]),

                "total_pages": len(processed_pages),

                "ocr_pages": sum(
                    1 for page in processed_pages
                    if page["source"] == "ocr"
                ),

                "languages": list({
                    page.get("language", "unknown")
                    for page in processed_pages
                })
            },

            "pages": processed_pages
        }

        # return {
        #     "document_id": str(uuid.uuid4()),
        #     "filename": os.path.basename(pdf_path),
        #     "pages": processed_pages
        # }
        # return processed_pages