from typing import Callable, NamedTuple

from io import BufferedIOBase


class Namespace(NamedTuple):
    input_file: BufferedIOBase
    output_file: BufferedIOBase
    width: int
    height: int
    func: Callable
