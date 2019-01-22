"""
This script was tested on Python 3.7
Author: Jorge Orpinel
"""


def flatten_deep(arr:list):
    """ Flattens arbitrarily-nested list `arr` into single-dimensional. """
    flat = []

    while arr:
        if isinstance(arr[0], list):  # Checks whether first element is a list
            arr = arr[0] + arr[1:]  # If so, flattens that first element one level
        else:
            flat.append(arr.pop(0))  # Otherwise add it to the flat array

    return flat


def flatten_trick(arr:list):
    """ Flattens arbitrarily-nested list `arr` via string trick.
    > Works well for nested lists that only contain integers. """
    import re

    arr_str = str(arr)
    return [int(s) for s in re.findall(r'\d+', arr_str)]


nested = [[1, 2, [3]], 4, [4, [[5]], 'p'], 99.5]
print(f'{nested}\n is properly flattened to:\n{flatten_deep(nested)}\n')

print(f'{nested}\n is trick-flattened to:\n{flatten_trick(nested)}\n')
