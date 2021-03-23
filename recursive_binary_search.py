import pandas as pd
import numpy as np

def recursive_binary_search(list, target):
    """ Returns the true if found, else returns None"""

    if len(list) == 0:
        return False
    else:
        midpt = (len(list))//2

        if list[midpt] == target:
            return True
        else:
            if list[midpt] < target:
                return recursive_binary_search(list[midpt + 1:], target)
            else:
                return recursive_binary_search(list[:midpt], target)


def verify(result):
    print("Target found: ", result)


numbers = [1, 2, 3, 4, 5, 6, 7, 8,12,15,20,32,40]

result = recursive_binary_search(numbers, 32)
verify(result)

result = recursive_binary_search(numbers, 25)
verify(result)