from f2i.cli import arguments
from f2i.functions import image_to_file


def register_reconvert_parser(subparser):
    parents = [
        arguments.create_input_file_argument(),
        arguments.create_output_file_argument(),
    ]

    convert_parser = subparser.add_parser('reconvert', help='reconvert image to file', parents=parents)
    convert_parser.set_defaults(func=image_to_file.reconvert)
