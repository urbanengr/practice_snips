def merge_sort(list):
    """
    Sorts a list in ascending order and Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    """

    if len(list) <= 1:      #check for single or no element list
        return list         #if single or no element no sort needed, return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge_sort(left, right)
