import fitz
from io import BytesIO


class ResumeParser:

    @staticmethod
    def extract_pdf_text(file_bytes: bytes) -> str:
        pdf = fitz.open(stream=BytesIO(file_bytes), filetype="pdf")

        text = ""

        for page in pdf:
            text += page.get_text()

        pdf.close()

        return text.strip()