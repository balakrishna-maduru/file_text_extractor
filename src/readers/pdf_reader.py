import io
from pathlib import Path
from typing import Optional, Dict
import fitz  # PyMuPDF for handling PDF and extracting images


class PDFReader:
    """PDF parser."""

    def __init__(self, return_full_document: Optional[bool] = False) -> None:
        """Initialize PDFReader."""
        self.return_full_document = return_full_document

    def load_data(
        self,
        file: Path,
        extra_info: Optional[Dict] = None,
        image_conversion_api: Optional[callable] = None,
    ) -> str:
        """Parse file and replace images with converted text."""
        if not isinstance(file, Path):
            file = Path(file)

        doc = fitz.open(file)
        full_text = []

        for page_index in range(len(doc)):
            page = doc.load_page(page_index)
            blocks = page.get_text("dict")["blocks"]  # Extract text blocks as dict

            content_items = []

            print(f"Processing page {page_index + 1}/{len(doc)}")

            # Process text blocks
            for block in blocks:
                if "lines" in block:
                    block_text = ""
                    for line in block["lines"]:
                        for span in line["spans"]:
                            block_text += span["text"]
                    content_items.append((float(block["bbox"][1]), block_text))  # Use y0 of the block as the position

            # Process image blocks using get_images and get_image_rects
            images = page.get_images(full=True)
            for img_index, img in enumerate(images):
                xref = img[0]  # The first item is the xref
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_filename = f"image_{page_index}_{xref}.png"

                # Save the image locally
                with open(image_filename, "wb") as image_file:
                    image_file.write(image_bytes)

                # Get the image's position using get_image_rects
                image_rects = page.get_image_rects(xref)
                if image_rects:
                    y0_position = image_rects[0].y0  # Use y0 from the first rect

                    # Process the image through the conversion API
                    if image_conversion_api:
                        extracted_text = image_conversion_api(image_filename)
                        print(f"Extracted text from image: {extracted_text[:50]}...")
                        content_items.append((y0_position, extracted_text))  # Use y0 of the image as the position

            # Sort all content items by their y-position (to maintain the order on the page)
            content_items.sort(key=lambda item: item[0])

            # Combine sorted content items
            page_content = [item[1] for item in content_items]
            page_text = "\n".join(page_content).strip()
            full_text.append(page_text)
            print(f"Page content length: {len(page_text)}")

        final_text = "\n".join(full_text)
        print(f"Final text length: {len(final_text)}")
        return final_text