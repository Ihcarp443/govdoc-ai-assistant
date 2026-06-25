# D:\project2\backend\services\document_ingestion.py
from providers.pdf.pdf_extractor import PDFExtractor
from providers.ocr.easyocr_provider import EasyOCRProvider
import os
import uuid

class DocumentIngestionService:

    def __init__(self):

        self.pdf_extractor = PDFExtractor()
        self.ocr_provider = EasyOCRProvider()

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

       

        return {
            "document_id": str(uuid.uuid4()),
            "filename": os.path.basename(pdf_path),
            "pages": processed_pages
        }
        # return processed_pages