'''
  Question : 
    - Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
    - You are given a target value to search. If found in the array return its index, otherwise return -1.
    - Must be O(logn) runtime
    
    Time Allocated : 25 minutes
    Time used : 50 minutes
    Status : completed but surpassed time limit
    
''''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # edge case
        if len(nums) == 0:
            return -1
        
        low = 0
        high = len(nums)
        middle = int((low + high)/2)
        if nums[middle] == target:
                return middle
        else:
            split_arr = self.split(nums,middle)
            
        
        first_split = split_arr[0]
        second_split = split_arr[1]
        
        if target > first_split[len(first_split)-1]:
            
            return self.binary_search(first_split, target, "first")
        else:
            return self.binary_search(second_split, target, "second")
                
        
    def split(self, arr, pivot):
        
        first_half = arr[0 : pivot]
        second_half = arr[pivot+1: ]
        
        return (first_half, second_half)
    
    def binary_search(self, arr, target, which_array):
        
        low = 0
        high = len(arr)
        while low <= high:
            middle = int((low + high)/2) - 1
            if arr[middle] == target:
                if which_array == "first":
                    return middle
                else:
                    return (middle + len(arr) + 1)
                
            elif arr[middle] > target:
                
                high = middle - 1 
            else:
                low = middle + 1 

        return -1
