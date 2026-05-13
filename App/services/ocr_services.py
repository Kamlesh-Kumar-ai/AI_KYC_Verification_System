import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import cv2

# Windows users:
# Uncomment and update path if needed

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

Poppler_path = r"C:\poppler\library\bin"

def prop_img(file_path):
    img = cv2.imread(file_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    threshold = cv2.threshold(
        gray,
        155,
        255,
        cv2.THRESH_BINARY
    )[1]
    return threshold
    

def extract_text(file_path: str):
    
    txt = ""

    if file_path.lower().endswith(".pdf"):


        pages = convert_from_path(
                file_path,
                poppler_path=Poppler_path
            )

        for page in pages:
            text += pytesseract.image_to_string(page)

    else:
        processed_image = prop_img(file_path)
        text = pytesseract.image_to_string(processed_image)
        return text