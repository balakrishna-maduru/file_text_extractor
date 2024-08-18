import pytesseract
from PIL import Image
import io

def image_conversion_api(image_stream: io.BytesIO) -> str:
    """Converts an in-memory image to text using Tesseract OCR."""
    # Load the image from the in-memory file-like object
    image = Image.open(image_stream)
    
    # Use Tesseract to extract text from the image
    extracted_text = pytesseract.image_to_string(image)
    
    return extracted_text