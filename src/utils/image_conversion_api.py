
import pytesseract
from PIL import Image

def image_conversion_api(image_path: str) -> str:
    image = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text
