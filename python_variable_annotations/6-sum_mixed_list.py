#!/usr/bin/env python3
"""file to add a mixed list of numbers

Returns:
    float: the final sum
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Function that adds all numbers in a list so long as they are integers
    or floats

    Args:
        mxd_list (List[Union[int, float]]): List of numbers that can hold
        integers or floats

    Returns:
        float: Final sum of all integers and floats
    """
    return sum(mxd_list)
