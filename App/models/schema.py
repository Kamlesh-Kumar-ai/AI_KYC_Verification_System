from pydantic import BaseModel

class OCRResponse(BaseModel):

    filename: str
    ocr_text: str
    parsed_data: dict
    is_valid_pan: bool