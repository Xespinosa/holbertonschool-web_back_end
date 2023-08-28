#!/usr/bin/env python3
from typing import List

"""importing list type

Returns:
    List
"""


def sum_list(input_list: List[float]) -> float:
    """function to add all elements of a list

    Args:
        input_list (List[float]): list of real numbers to be added

    Returns:
        float: the sum of all floats in the list
    """
    return sum(input_list)
