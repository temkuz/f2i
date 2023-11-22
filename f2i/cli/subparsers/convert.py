from f2i.cli import arguments
from f2i.functions import file_to_image


def register_convert_parser(subparser):
    parents = [
        arguments.create_input_file_argument(),
        arguments.create_output_file_argument(),
        arguments.create_resolution_arguments()
    ]

    convert_parser = subparser.add_parser('convert', help='convert file to image', parents=parents)
    convert_parser.set_defaults(func=file_to_image.convert)
