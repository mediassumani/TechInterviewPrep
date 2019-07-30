'''
You are given a matrix with M rows and N columns.
Elements in matrix can be either 1 or 0.
Each row and column of matrix is sorted in ascending order. Find number of 0-s in the given matrix 
'''

def find_zeross(matrix):

    zero_counter = 0
    for sub_arr in matrix:

        # No need to check rest of arr if first element is a 1
        if sub_arr[0] == 1:
            continue

        for elem in sub_arr:
            if elem == 0:
                zero_counter += 1

    return zero_counter

def main():
    
    matrix = [
        [0, 1],
        [1, 1, 1, 1],
        [0, 0, 1, 1],
        [0, 1, 1, 1],
        [0, 0, 1, 1]
    ]
    
    print(find_zeross(matrix))
    
    
if __name__ == "__main__":
    main()