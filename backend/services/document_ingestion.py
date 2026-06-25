from providers.pdf.pdf_extractor import PDFExtractor
from providers.ocr.easyocr_provider import EasyOCRProvider


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

            if len(extracted_text) < 100:

                extracted_text = self.ocr_provider.extract_text(
                    page["image_path"]
                )

                source = "ocr"

            processed_pages.append({
                "page": page["page"],
                "source": source,
                "text": extracted_text
            })

        return processed_pages