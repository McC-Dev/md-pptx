from md_pptx.utilities.meta_parser import MetaData
from md_pptx.utilities.exceptions import MissingDataException
from yaml import safe_load


class MdParser:
    """
    Splits the md file into blocks that can be used and identified by other functions/objects.
    """

    def __init__(self, input_file: str):
        self.input_file = input_file
        with open(self.input_file) as input_file_data:
            input_file_data = input_file_data.read().strip()

        input_file_data = input_file_data.replace("\t", "    ")
        sections = input_file_data.split("\n# ")

        self.meta_data = self.parse_yaml_data(sections[0], True)

        slides_dict = {}
        for slide_number, slide_data in enumerate(sections[1:]):
            each_slide_dict = {}
            lines = slide_data.split("\n\n")
            slide_title = lines[0]
            each_slide_dict["title"] = slide_title
            for line_number, line in enumerate(lines[1:]):
                if line.startswith("#"):
                    level, header = self.parse_headers(line)
                    each_slide_dict[f'{line_number}_header_{level}'] = header
                    continue
                if line.startswith('-'):
                    self.parse_bullets
                    print(line)
                print("\n\n")

            slides_dict[slide_number + 1] = each_slide_dict
        # print(parsed_file.input_file_data.split("\n# ")[1].split("\n\n"))

    def parse_yaml_data(self, file_data: str, file_header: bool) -> MetaData:
        if not file_data.startswith("---"):
            raise MissingDataException("No meta data found at start of file")

        meta_data_yaml = safe_load(file_data.split("---\n")[1])

        return MetaData(**meta_data_yaml, is_file_header=file_header)

    def parse_headers(self, line_data: str):
        header_data = line_data.lstrip("#")
        level = len(line_data) - len(header_data)
        return level, header_data.lstrip()

    def parse_bullets(self, line_data: str):
        pass

if __name__ == "__main__":
    parsed_file = MdParser("tests/TestCase.md")
