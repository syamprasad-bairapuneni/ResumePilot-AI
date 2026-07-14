import re


class JDService:

    @staticmethod
    def parse_jd(text: str):

        skills = JDService.extract_skills(text)

        responsibilities = JDService.extract_responsibilities(text)

        return {
            "job_title": JDService.extract_job_title(text),
            "company": JDService.extract_company(text),
            "required_skills": skills,
            "preferred_skills": [],
            "responsibilities": responsibilities,
            "keywords": skills
        }

    @staticmethod
    def extract_job_title(text):

        lines = text.split("\n")

        for line in lines:

            line = line.strip()

            if line and len(line) < 80:
                return line

        return ""

    @staticmethod
    def extract_company(text):

        match = re.search(r"Who we are.*?Volvo Group", text, re.IGNORECASE | re.DOTALL)

        if match:
            return "Volvo Group"

        return ""

    @staticmethod
    def extract_skills(text):

        common_skills = [

            "Python",
            "SQL",
            "Power BI",
            "Excel",
            "Java",
            "C#",
            "React",
            "Angular",
            "JavaScript",
            "HTML",
            "CSS",
            "Power Automate",
            "AI",
            "ML",
            "Machine Learning",
            "Data Analysis",
            "Data Science",
            "Automation",
            "Qlik"

        ]

        skills = []

        text_lower = text.lower()

        for skill in common_skills:

            if skill.lower() in text_lower:
                skills.append(skill)

        return sorted(list(set(skills)))

    @staticmethod
    def extract_responsibilities(text):

        responsibilities = []

        lines = text.split("\n")

        capture = False

        for line in lines:

            line = line.strip()

            if "What you will do" in line:
                capture = True
                continue

            if "Who You Are" in line:
                break

            if capture:

                if line:
                    responsibilities.append(line)

        return responsibilities