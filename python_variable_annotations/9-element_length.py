#!/usr/bin/env python3
"""Holds a function that returns the length of a list

Returns:
    _type_: _description_
"""


from typing import Sequence, Tuple, Iterable, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that iterates through a List or Tuple and returns the length

    Args:
        lst (Iterable[Sequence]): Sequence of data (Tuple or List) to be
        iterated

    Returns:
        List[Tuple[Sequence, int]]: Length of the whole sequence
    """
    return [(i, len(i)) for i in lst]
