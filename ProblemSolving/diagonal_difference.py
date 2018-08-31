# Problem # 4 : Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# Category : Easy
# Allocated time : 45 minutes
# Time used : 37 minute

import math

# n is the number or rows and columns and matrix is the multi-dimentional array
def diagonal_difference(n, matrix):
    left_to_right_sum = 0
    right_to_left_sum = 0
    counter = 1
    for row in range(len(matrix)):
        temp_array = matrix[row]
        for col in range(len(matrix)):
            right_to_left_sum += temp_array[n-counter]
            left_to_right_sum += temp_array[counter - 1]
            counter += 1
            break
    return (math.fabs(left_to_right_sum - right_to_left_sum))

def main():

    matrix = [[1,2,3],[4,5,6],[9,8,9]]
    print(diagonal_difference(3,matrix)) #prints 2.0

if __name__ == '__main__':
    main()
