from md_pptx.utilities.meta_parser import parse_meta_data


class md_parser:
    def __init__(self, input_file: str, output_file: str):
        self.input_file = input_file
        with open(self.input_file) as input_file_data:
            self.input_file_data = input_file_data.read()

        self.meta_data = parse_meta_data(self.input_file_data.strip())

        # self.output_file = output_file


if __name__ == "__main__":
    parsed_file = md_parser("tests/TestCase.md", "")
    print(parsed_file.meta_data.colours)
    print(type(parsed_file.meta_data.colours["Accent2"]))