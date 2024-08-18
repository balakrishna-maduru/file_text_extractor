import unittest
from pathlib import Path
from src.readers.word_reader import WordReader

class TestWordReader(unittest.TestCase):

    def test_word_reader(self):
        reader = WordReader()
        text = reader.load_data(Path("data/docx/sample.docx"))
        self.assertGreater(len(text), 0)
        self.assertNotIn("[IMAGE_", text)

if __name__ == '__main__':
    unittest.main()