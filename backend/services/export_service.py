from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class ExportService:

    def __init__(self):
        pass

    def create_docx(self,report_text: str,file_name: str = "report.docx") -> str:

        doc = Document()

        for line in report_text.split("\n"):

            line = line.strip()
            if not line:
                continue

            if ":" in line:
                title, content = line.split(":", 1)
                doc.add_heading(title.strip(), level=1)
                doc.add_paragraph(content.strip())
            else:

                doc.add_paragraph(line)

        doc.save(file_name)
        return file_name

    def create_pdf(self,report_text: str,file_name: str = "report.pdf") -> str:

        pdf = canvas.Canvas(file_name,pagesize=letter)
        width, height = letter

        y = height - 50

        for line in report_text.split("\n"):
            if y < 50:
                pdf.showPage()
                y = height - 50

            pdf.drawString(50, y, line)
            y -= 18

        pdf.save()
        return file_name

    def export(self,text: str,file_type: str,file_name: str):

        if file_type.lower() == "pdf":
            return self.create_pdf(text, f"{file_name}.pdf")

        elif file_type.lower() == "docx":
            return self.create_docx(text, f"{file_name}.docx")

        raise ValueError("Unsupported format")