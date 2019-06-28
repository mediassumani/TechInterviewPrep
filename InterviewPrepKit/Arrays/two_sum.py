class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        indexes = []
        if not nums:
            return None
        
        for index, val in enumerate(nums):
            other_val = target - val
            if (other_val in nums) and (nums.index(other_val) != index):
                indexes.append(index)
                indexes.append(nums.index(other_val))
                break

        return indexes