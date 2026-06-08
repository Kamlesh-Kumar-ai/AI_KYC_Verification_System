import re

def classify_document(text):

    text_upper = text.upper()

    pan_pattern = r"\b[A-Z]{5}[0-9]{4}[A-Z]\b"

    aadhaar_pattern = r"\b\d{4}\s?\d{4}\s?\d{4}\b"

    if re.search(
        pan_pattern,
        text_upper
    ):
        return "PAN"

    if re.search(
        aadhaar_pattern,
        text
    ):
        return "AADHAAR"

    if "AADHAAR" in text_upper:
        return "AADHAAR"

    if "GOVERNMENT OF INDIA" in text_upper:
        return "AADHAAR"

    if "INCOME TAX" or "INCOME TAX DEPARTMENT" in text_upper:
        return "PAN"

    return "UNKNOWN"