from PIL import Image

from f2i.classes.namespace import Namespace
from f2i.variables.color import RGBColor, convert_table


def _convert_int_to_pairs(value: int) -> tuple[int, int, int, int]:
    r1 = value >> 6 & 3
    r2 = value >> 4 & 3
    r3 = value >> 2 & 3
    r4 = value & 3
    return r1, r2, r3, r4


def _convert_int_to_color(value: int) -> list[RGBColor]:
    return [convert_table[i] for i in _convert_int_to_pairs(value)]


def _convert_bytes_to_image(value: bytes) -> list[RGBColor]:
    result = []
    for i in value:
        result.extend(_convert_int_to_color(i))
    return result


def convert(namespace: Namespace):
    with namespace.input_file as f:
        image_data = _convert_bytes_to_image(f.read())

    width = namespace.width
    height = namespace.height

    image = Image.new('RGB', size=(width, height))
    image.putdata(image_data)
    image.save(namespace.output_file)
