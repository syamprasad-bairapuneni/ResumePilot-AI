import re


def extract_email(text: str):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    match = re.search(pattern, text)
    return match.group(0) if match else None


def extract_phone(text: str):
    pattern = r"(\+91[- ]?)?[6-9]\d{9}"
    match = re.search(pattern, text)
    return match.group(0) if match else None