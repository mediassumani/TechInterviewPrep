'''Given an array of integers nums sorted in ascending order,
 find the starting and ending position of a given target value.'''

# Time Complexity : O(n)
# Space Complexity : O(1)
def find_first_last(arr, target):

    target_indexes = []
    for i in range(len(arr)):
        if arr[i] == target:
            target_indexes.append(i)

    if len(target_indexes) == 0:
        return [-1, -1]

    first = target_indexes[0]
    last = target_indexes[len(target_indexes)-1]
    return [first, last]
