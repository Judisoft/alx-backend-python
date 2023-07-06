#!/usr/bin/env python3
"""return a turple"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a string k and an int OR float v as arguments and returns a tuple"""
    new_tup: Tuple[str, Union[int, float]] = (k, v**2)
    return new_tup
