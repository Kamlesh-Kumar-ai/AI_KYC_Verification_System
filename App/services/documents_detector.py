def detect_document(text):

    text = text.lower()

    if "income tax department" in text:
        return "PAN"

    if "government of india" in text:
        return "AADHAAR"

    return "UNKNOWN"