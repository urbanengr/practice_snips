import pandas as pd
import numpy as np

def binary_search(list, target):
    """ Returns the index position of the target if found, else returns None"""

    first = 0
    last = len(list) - 1

    while first <= last:
        midpt = (first + last)//2

        if list[midpt] == target:
            return midpt
        elif list[midpt] < target:
            first = midpt + 1
        else:
            last = midpt -1

    return None

def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in list")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)