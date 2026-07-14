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

def extract_education(text: str):

    education = []

    lines = text.split("\n")

    for i, line in enumerate(lines):

        line = line.strip()

        if (
            "B.Tech" in line
            or "Bachelor" in line
            or "Intermediate" in line
            or "Diploma" in line
            or "M.Tech" in line
            or "MBA" in line
        ):

            institution = ""
            score = ""
            year = ""

            if i + 1 < len(lines):
                institution = lines[i + 1].strip()

            import re

            score_match = re.search(r"(CGPA|GPA)\s*[:\-]?\s*([\d.]+)", institution)

            if score_match:
                score = score_match.group(2)

            year_match = re.search(r"(19|20)\d{2}", institution)

            if year_match:
                year = year_match.group()

            education.append(
                {
                    "degree": line,
                    "institution": institution,
                    "score": score,
                    "year": year,
                }
            )

    return education

def extract_experience(text: str):

    experience = []

    lines = text.split("\n")

    inside_experience = False

    current = {}

    for line in lines:

        line = line.strip()

        if "EXPERIENCE" in line.upper():
            inside_experience = True
            continue

        if "PROJECTS" in line.upper():
            break

        if inside_experience:

            if "|" in line:

                parts = line.split("|")

                current = {
                    "role": parts[0].strip(),
                    "company": parts[1].strip() if len(parts) > 1 else "",
                    "duration": ""
                }

            elif "Duration" in line:

                current["duration"] = line.replace("Duration:", "").strip()

                experience.append(current)

    return experience