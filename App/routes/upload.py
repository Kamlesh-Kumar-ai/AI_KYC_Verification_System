from fastapi import APIRouter, UploadFile, File
import shutil
import os

from App.services.ocr_services import extract_text
from App.services.parser import extract_pan_details
from App.services.validator import validate_pan

router = APIRouter()

UPLOAD_DIR = "data/uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # OCR extraction
    extracted_text = extract_text(file_path)

    # Parse PAN details
    parsed_data = extract_pan_details(extracted_text)

    # Validate PAN
    is_valid_pan = validate_pan(parsed_data.get("pan_number"))

    return {
        "filename": file.filename,
        "ocr_text": extracted_text,
        "parsed_data": parsed_data,
        "is_valid_pan": is_valid_pan
    }