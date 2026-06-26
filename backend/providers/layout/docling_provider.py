# D:\project2\backend\providers\layout\docling_provider.py
from docling.document_converter import DocumentConverter


class DoclingProvider:

    def __init__(self):
        self.converter = DocumentConverter()

    def extract_layout(self, pdf_path):

        result = self.converter.convert(pdf_path)

        return result.document.export_to_markdown()