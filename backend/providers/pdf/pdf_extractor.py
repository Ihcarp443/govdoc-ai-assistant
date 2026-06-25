import fitz
import os


class PDFExtractor:

    def split_pdf_pages(self, pdf_path, output_folder):

        os.makedirs(output_folder, exist_ok=True)

        doc = fitz.open(pdf_path)

        pages = []

        for page_num in range(len(doc)):

            page = doc[page_num]

            text = page.get_text().strip()

            image_path = os.path.join(
                output_folder,
                f"page_{page_num+1}.png"
            )

            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            pix.save(image_path)

            pages.append({
                "page": page_num + 1,
                "text": text,
                "image_path": image_path
            })

        return pages