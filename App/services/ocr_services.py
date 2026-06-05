import pytesseract
from pdf2image import convert_from_path
import cv2
import os

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

POPPLER_PATH = r"C:\poppler\Library\bin"


def preprocess_image(file_path):

    img = cv2.imread(file_path)

    if img is None:
        raise ValueError(
            f"Could not load image from: {file_path}"
        )

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    _, threshold = cv2.threshold(
        gray,
        155,
        255,
        cv2.THRESH_BINARY
    )

    return threshold


def extract_text(file_path):

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    # PDF Processing
    if file_path.lower().endswith(".pdf"):

        pages = convert_from_path(
            file_path,
            poppler_path=POPPLER_PATH
        )

        text = ""

        for page in pages:
            text += pytesseract.image_to_string(page)

        return text

    # Image Processing
    processed_image = preprocess_image(file_path)

    text = pytesseract.image_to_string(
        processed_image
    )

    return text