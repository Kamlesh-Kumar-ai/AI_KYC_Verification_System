import re

def extract_aadhaar(text):

    pattern = r"\b\d{4}\s?\d{4}\s?\d{4}\b"

    match = re.search(
        pattern,
        text
    )

    if match:

        aadhaar_number = (
            match.group()
            .replace(" ", "")
        )

        return aadhaar_number

    return None