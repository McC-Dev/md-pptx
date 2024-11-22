import yaml
from md_pptx.utilities.exceptions import MissingDataException
from PIL import ImageColor
import logging

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s"
)


class MetaData:
    def __init__(
        self,
        **kwargs,
    ):
        for key, value in kwargs.items():
            if value is None:
                continue
            setattr(self, key.lower(), value)

        if self.colours:
            self.colours = self.define_colours(self.colours)

        logging.debug(self.__dict__)

    def define_colours(self, Colours: list[str,]) -> dict[str, str | None]:
        colour_dict = {
            "Background1": None,
            "Background2": None,
            "Dark1": None,
            "Dark2": None,
            "Accent1": None,
            "Accent2": None,
            "Accent3": None,
            "Accent4": None,
            "Accent5": None,
            "Accent6": None,
        }
        for key, value in Colours.items():
            try:
                colour_dict[key] = ImageColor.getrgb(value)
            except (KeyError, ValueError):
                continue
        return colour_dict


def parse_meta_data(file_data: str) -> MetaData:
    if not file_data.startswith("---"):
        raise MissingDataException("No meta data found at start of file")

    meta_data_yaml = yaml.safe_load(file_data.split("---\n")[1])

    return MetaData(**meta_data_yaml)
