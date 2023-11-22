from argparse import ArgumentParser
from sys import argv

from f2i.cli import subparsers


def parse_args():
    default_parser = ArgumentParser()
    subparser = default_parser.add_subparsers()

    subparsers.register_convert_parser(subparser)
    subparsers.register_reconvert_parser(subparser)

    if len(argv) == 1:
        default_parser.print_help()
        exit()

    return default_parser.parse_args()
