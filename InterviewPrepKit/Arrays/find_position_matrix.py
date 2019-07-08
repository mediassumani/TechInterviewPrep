
'''
Given a matrix mat[][] of size m * n which is sorted in row-wise fashion and an array row[],
the task is to check if any row in the matrix is equal to the given array row[].

'''
# assume : row size != col size
# Matched row in matrix must be same order as input arr
# assume == sign O(n)
def find_row(matrix, row): # O(n^3)
    
    for index, curr_row in enumerate(matrix): # O(n) time

        if len(curr_row) == len(row):
            left = 0
            right = len(row) - 1
            while left <= right:
                if (row[left] != curr_row[left]) and (row[right] != curr_row[right]):
                    return None
                left +=1
                right -= 1
            return index + 1
    return None


def main():
    
    matrix = [[1,2,3,4],
              [4,3,2,1],
              [4,8,5,0,1,34],
              [4,3,2]]

    row = [4,3,2]
    print(find_row(matrix, row))

if __name__ == "__main__":
    main()