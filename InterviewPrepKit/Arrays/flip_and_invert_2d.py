'''
Given a binary matrix A, we want to flip the image horizontally,
then invert it, and return the resulting image.

'''

class Solution(object):
    
    def invert(self, arr):
        # O(n) Time | O(1) space
        for index, num in enumerate(arr):
            if num == 0:
                arr[index] = 1 
            elif num == 1:
                arr[index] = 0
            else:
                print("Not a binary")
                
                
    def flip(self, arr):
        arr.reverse() # O(n) time | O(1) spae
        
    def flipAndInvertImage(self, A):
        # O(n^2) time | O(1) space
        for arr in A: # O(n)
            self.flip(arr) # flip the current array - O(n)
            self.invert(arr) # invert the current array O(n)
            
        return A