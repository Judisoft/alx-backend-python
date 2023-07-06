#!/usr/bin/env python3
"""returns sum of of a list """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Sums list of floats """
    sum: float = 0
    for i in input_list:
        sum += i
    return sum
