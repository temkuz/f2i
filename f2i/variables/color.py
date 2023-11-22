from f2i.classes.color import RGBColor

RED_COLOR = RGBColor(255, 0, 0)
GREEN_COLOR = RGBColor(0, 255, 0)
BLUE_COLOR = RGBColor(0, 0, 255)
WHITE_COLOR = RGBColor(255, 255, 255)

BLACK_COLOR = RGBColor(0, 0, 0)

convert_table = {
    0: RED_COLOR,
    1: GREEN_COLOR,
    2: BLUE_COLOR,
    3: WHITE_COLOR
}

reconvert_table = {v: k for k, v in convert_table.items()}
