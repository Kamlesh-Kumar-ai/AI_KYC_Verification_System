import re

def validate_aadhaar(aadhaar_number):

    if not aadhaar_number:
        return False

    aadhaar_number = (
        aadhaar_number
        .replace(" ", "")
        .replace("-", "")
    )

    return bool(
        re.fullmatch(
            r"\d{12}",
            aadhaar_number
        )
    )