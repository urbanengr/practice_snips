# Practice Code Snippets
This repo contains snippets from learning and practice lessons

### Nanodegree
Programming for Data Science with Python

### Date created
linear_search.py - March 23, 2021
binary_search.py - March 23, 2021  
recursive_binary_search.py - March 23, 2021
linked_list.py - March 24, 2021
merge_sort.py - March 25, 2021

### Software versions
Python v3.8.3


## *_search.py programs
Learned about Big'O' notation and the different time/space complexities for various search algorithms.

## linked_lists.py
Introduced to the concept of linked lists.

#### code description
The initial commit is a node object as a starting building block.

```
data = None         #instance variable holds stored data 
next_node = None    #instance variable points to next node in list
```

## merge_sort.py
Uses the 'divide and conquer' strategy recursively breaking down a list into multiple single element lists. Then merges the lists while sorting in the process.

#### code description
The code description annotates code bits for clarity. This is *not* the entire proram.

```
if len(list) <= 1:      #check for single or no element list
    return list         #if single or no element no sort needed, return list
	
	
mid = len(list)//2      #use floor function to find midpoint of list


i = 0                   #tracks left list indices
j = 0                   #tracks right list indices


if left[i] < right[j]:  #if element in right half is greater
    l.append(left[i])   #move to end of left half
	
else:
    l.append(right[j])  #move left element to end of right half
	

while i < len(left):    #if right half is shorter than left
    l.append(left[i])   #assumes elements are sorted	
	
	
while j < len(right):   #for left half is shorter than right
    l.append(right[j])  #assumes elements are sorted


return (list[0] < list[1]) and verify_sorted(list[1:])	#uses recursion
```

### Credits
Youtube video - "Algorithms and Data Structures - Full Course for Beginners from Treehouse", posted March 18, 2021

