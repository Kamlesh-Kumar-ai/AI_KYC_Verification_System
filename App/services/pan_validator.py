import re

def validate_pan(pan_number):

    if not pan_number:
        return False

    pan_number = pan_number.strip().upper()

    pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]$"

    return bool(
        re.fullmatch(pattern, pan_number)
    )