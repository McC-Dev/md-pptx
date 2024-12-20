from md_pptx import md_parser
import unittest


class MetaDataTest(unittest.TestCase):
    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        parsed_file = md_parser.MdParser("./tests/TestCase.md")
        self.meta_data = parsed_file.meta_data

    def test_title(self):
        self.assertEqual(self.meta_data.title, "PowerPoint TestCase")

    def test_colours(self):
        self.assertEqual(self.meta_data.colours["Accent2"], (227, 6, 19))

    def test_empty_field_is_removed(self):
        self.assertFalse("unexpectedfield" in self.meta_data.__dict__)


if __name__ == "__main__":
    unittest.main()
