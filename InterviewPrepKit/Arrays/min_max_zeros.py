# Reference question : https://www.geeksforgeeks.org/find-row-with-maximum-and-minimum-number-of-zeroes-in-given-matrix/
def find(arr):
    
    counter = 0
    for val in arr:
        if val == 0:
            counter += 1

    return counter

def find_max_min(matrix):
    
    result_list = []
    for arr in matrix: # O(n)
        result_list.append(find(arr))# O(n)
    
    return(min(result_list), max(result_list))