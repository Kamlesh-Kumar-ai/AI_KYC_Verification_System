import re

def validate_pan(pan_number: str):

    if not pan_number:
        return False

    pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]$"

    return bool(re.match(pattern, pan_number))