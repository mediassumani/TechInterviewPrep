'''
Given a sorted array and a target value,
return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
'''


class Solution(object):
    
    def searchInsert(self, nums, target):
        found = False
        # O(n) - Perform linear search to find if the element is present
        for index, num in enumerate(nums):
            if num == target:
                return index
        counter = 0
        if not found:
            #O(n) - Traverse arr to check if elements are > than the target
            for index, num in enumerate(nums):
                if target > num:
                    counter += 1       
        return counter
    