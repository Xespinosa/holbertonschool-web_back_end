#!/usr/bin/env python3
"""file to hold a multiplying fucntion

Returns:
    Function: Muliplier function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function that calls the multiplier function

    Args:
        multiplier (float): Number that is to be mulitplied

    Returns:
        Callable[[float], float]: Function that multiplies
    """
    def multiplier_function(d: float) -> float:
        """Function that multiplies a number

        Args:
            d (float): number to be multiplied

        Returns:
            float: multiplication result
        """
        return d * multiplier
    return multiplier_function
