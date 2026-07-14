import re

# -----------------------------
# Email
# -----------------------------
def extract_email(text: str):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    match = re.search(pattern, text)
    return match.group(0) if match else None


# -----------------------------
# Phone
# -----------------------------
def extract_phone(text: str):
    pattern = r"(\+91[- ]?)?[6-9]\d{9}"
    match = re.search(pattern, text)
    return match.group(0) if match else None


# -----------------------------
# Name
# -----------------------------
def extract_name(text: str):

    match = re.search(r"Name\s*:\s*(.+)", text, re.IGNORECASE)

    if match:
        return match.group(1).strip()

    lines = text.split("\n")

    for line in lines[:10]:

        line = line.strip()

        if (
            line
            and "@" not in line
            and "email" not in line.lower()
            and "phone" not in line.lower()
            and "location" not in line.lower()
            and len(line.split()) <= 4
        ):
            return line

    return None


# -----------------------------
# Location
# -----------------------------
def extract_location(text: str):

    match = re.search(r"Location\s*:\s*(.+)", text, re.IGNORECASE)

    if match:
        return match.group(1).strip()

    return None


# -----------------------------
# Skills
# -----------------------------
COMMON_SKILLS = [

    "Python",
    "SQL",
    "MySQL",
    "SQL Server",
    "Power BI",
    "Excel",
    "Java",
    "C#",
    "React",
    "Angular",
    "JavaScript",
    "HTML",
    "CSS",
    "ASP.NET Core",
    "ASP.Net Core",
    "Entity Framework Core",
    "MVC",
    "Web API",
    "FastAPI",
    "Flask",
    "Git",
    "GitHub",
    "Docker",
    "Azure",
    "Power Automate"

]


def extract_skills(text: str):

    text_lower = text.lower()

    skills = []

    for skill in COMMON_SKILLS:

        if skill.lower() in text_lower:
            skills.append(skill)

    return sorted(list(set(skills)))