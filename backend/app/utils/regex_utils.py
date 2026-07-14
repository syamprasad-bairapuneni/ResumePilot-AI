import re


def extract_email(text: str):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    match = re.search(pattern, text)
    return match.group(0) if match else None


def extract_phone(text: str):
    pattern = r"(\+91[- ]?)?[6-9]\d{9}"
    match = re.search(pattern, text)
    return match.group(0) if match else None


def extract_name(text: str):
    import re

    # Look for "Name: John Doe"
    match = re.search(r"Name\s*:\s*(.+)", text, re.IGNORECASE)

    if match:
        return match.group(1).strip()

    # Fallback
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


def extract_location(text: str):
    match = re.search(r"Location[:\s]+([^\n]+)", text, re.IGNORECASE)

    if match:
        return match.group(1).strip()

    return None