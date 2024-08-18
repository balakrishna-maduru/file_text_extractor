import unittest
from pathlib import Path
from src.readers.pdf_reader import PDFReader

class TestPDFReader(unittest.TestCase):

    def test_pdf_reader(self):
        reader = PDFReader(return_full_document=True)
        text = reader.load_data(Path("data/pdfs/sample.pdf"))
        self.assertGreater(len(text), 0)
        self.assertNotIn("[IMAGE_", text)

if __name__ == '__main__':
    unittest.main()