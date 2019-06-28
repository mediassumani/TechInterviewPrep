
'''
Given a sorted array nums, remove the duplicates in-place and return the new length.
You must do this by modifying the input array in-place with O(1) extra memory.
Do not allocate extra space for a new array
'''
class Solution(object):
    def removeDuplicates(self, nums):
   
        if len(nums) == 0:
            return None
        
        seens = {}
        index = 0

        while index < len(nums):
    
            value = nums[index]
            if value not in seens:
                seens[value] = 1
                
            elif value in seens:
                del nums[index]
                index -= 1   
            index+= 1
      
        return len(nums) 