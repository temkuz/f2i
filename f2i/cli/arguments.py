from argparse import ArgumentParser, FileType


def create_input_file_argument():
    parser = ArgumentParser(add_help=False)
    parser.add_argument('input_file', help='input file', type=FileType('rb'))
    return parser


def create_output_file_argument():
    parser = ArgumentParser(add_help=False)
    parser.add_argument('output_file', help='output file', type=FileType('wb'))
    return parser


def create_resolution_arguments():
    parser = ArgumentParser(add_help=False)

    group = parser.add_argument_group(title='image resolution')
    group.add_argument('-W', '--width', help='image width (default:1920)', default=1920, type=int)
    group.add_argument('-H', '--height', help='image height (default:1080)', default=1080, type=int)

    return parser
