import re

def extract_pan(text):

    pan_pattern = r"\b[A-Z]{5}[0-9]{4}[A-Z]\b"

    match = re.search(
        pan_pattern,
        text.upper()
    )

    if match:
        return match.group()

    return None