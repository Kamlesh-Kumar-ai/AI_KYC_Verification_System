import re

def extract_pan_details(text: str):

    pan_pattern = r"[A-Z]{5}[0-9]{4}[A-Z]"
    aadhar_pattern = r"\d\d{4}\s\d{4}\s\d{4}"
    dob_pattern = r"\d{2}/\d{2}/\d{4}"

    pan_match = re.search(pan_pattern, text)
    aadhar_match = re.search(aadhar_pattern, text)
    dob_match = re.search(dob_pattern, text)

    pan_number = pan_match.group() if pan_match else None
    aadhar_number = aadhar_match.group() if aadhar_match else None
    dob = dob_match.group() if dob_match else None


    return {
        "pan_number": pan_number,
        "aadhar_number": aadhar_number,
        "dob" : dob
    }