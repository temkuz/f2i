from PIL import Image

from f2i.classes.namespace import Namespace
from f2i.variables.color import RGBColor, BLACK_COLOR, reconvert_table


def _get_colors(image) -> list[RGBColor]:
    width, height = image.size
    return [image.getpixel((x, y)) for y in range(height) for x in range(width)]


def _get_int(value: list[RGBColor]) -> bytes:
    result = 0
    for value in value:
        result = result << 2
        result += reconvert_table[value]
    return result.to_bytes()


def reconvert(namespace: Namespace):
    image = Image.open(namespace.input_file).convert('RGB')
    colors = _get_colors(image)
    file_data = b''
    for index in range(0, len(colors), 4):
        if colors[index] == BLACK_COLOR:
            break
        value = colors[index:index + 4]
        file_data += _get_int(value)

    with namespace.output_file as f:
        f.write(file_data)
