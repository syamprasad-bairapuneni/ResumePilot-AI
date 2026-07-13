from app.utils.regex_utils import extract_email, extract_phone


class ResumeService:

    @staticmethod
    def parse_resume(text: str):

        return {
            "email": extract_email(text),
            "phone": extract_phone(text)
        }