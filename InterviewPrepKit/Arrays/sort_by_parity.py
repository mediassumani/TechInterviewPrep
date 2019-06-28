class Solution(object):
    def sortArrayByParity(self, A):
        # O(n) time | O(n) space
        arr_even = []
        arr_odd = []
        
        for num in A:
            if num % 2 == 0:
                arr_even.append(num)
                
            if num % 2 == 1:
                arr_odd.append(num)  
                
        return arr_even + arr_odd