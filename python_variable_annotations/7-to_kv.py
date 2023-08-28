#!/usr/bin/env python3
"""creating tuples

Returns:
    Tuple: Tuple
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function to convert string and number to a tuple

    Args:
        k (str): String to be saved
        v (Union[int, float]): number (integer or float) to be saved

    Returns:
        Tuple[str, float]: Resulting tuple with the string and the square of
        the number
    """
    return tuple([k, v*v])
