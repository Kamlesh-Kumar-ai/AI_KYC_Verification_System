from App.services.pan_extractor import extract_pan
from App.services.aadhar_extractor import extract_aadhaar
from App.services.documents_classifier import classify_document


def parse_document(text):

    document_type = classify_document(text)

    result = {
        "document_type": document_type,
        "pan_number": None,
        "aadhaar_number": None
    }

    if document_type == "PAN":

        result["pan_number"] = extract_pan(
            text
        )

    elif document_type == "AADHAAR":

        result["aadhaar_number"] = (
            extract_aadhaar(text)
        )

    return result