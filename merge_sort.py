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

    return merge(left, right)


def split(list):
    """ Divide the unsorted list at midpoint into sublists.
     Returns two sublists - left and right """

    mid = len(list)//2      #use floor function to find midpoint of list
    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    """ Merges two lists, sorting them in the process
      Returns a new merged list"""

    l = []
    i = 0           #tracks left list indices
    j = 0           #tracks right list indices

    while i < len(left) and j < len(right):
        if left[i] < right[j]:      #if element in right half is greater
            l.append(left[i])       #move to end of left half
            i += 1
        else:
            l.append(right[j])      #move left element to end of right half
            j += 1

    """ Create while loops to catch uneven halves that will cause above loop to end"""

    while i < len(left):            #if right half is shorter than left
        l.append(left[i])           #assumes elements are sorted
        i += 1

    while j < len(right):        #for left half is shorter than right
        l.append(right[j])          #assumes elements are sorted
        j += 1

    return l

alist = [54, 26, 62, 45, 74, 3, 20, 25, 1]
l = merge_sort(alist)
print(l)

