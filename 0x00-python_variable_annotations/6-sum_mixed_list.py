#!/usr/bin/env python3
"""returns sum as float"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes a list of mixed ints and floats and returns the sum as a float"""
    sum: float = 0
    for i in mxd_lst:
        sum += i
    return sum
