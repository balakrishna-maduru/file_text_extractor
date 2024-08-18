

from pathlib import Path
from src.readers.pdf_reader import PDFReader
from src.readers.word_reader import WordReader
from src.utils.image_conversion_api import image_conversion_api

def main():
    # Process a PDF file
    pdf_reader = PDFReader()
    pdf_text = pdf_reader.load_data(Path("data/pdfs/example.pdf"), image_conversion_api=image_conversion_api)
    print("PDF Text:\n", pdf_text)

    # Process a DOCX file
    # word_reader = WordReader()
    # word_text = word_reader.load_data(Path("data/docx/example.docx"), image_conversion_api=image_conversion_api)
    # print("DOCX Text:\n", word_text)

if __name__ == "__main__":
    main()