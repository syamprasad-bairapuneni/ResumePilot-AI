from app.utils.regex_utils import (
    extract_name,
    extract_email,
    extract_phone,
    extract_location,
    extract_skills,
    extract_education,
    extract_experience
)


class ResumeService:

    @staticmethod
    def parse_resume(text: str):

        return {

    "personal_info": {

        "name": extract_name(text),

        "email": extract_email(text),

        "phone": extract_phone(text),

        "location": extract_location(text)

    },

    "skills": extract_skills(text),

    "education": extract_education(text),

    "experience": extract_experience(text)

}