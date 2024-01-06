from typing import List, Set, Dict, Union, Optional

Number = Union[int, float]


def indent(line: str, amount: int) -> str:
    indented_line: str = ' ' * amount + line
    return indented_line


def typing(number: Number):
    return number
