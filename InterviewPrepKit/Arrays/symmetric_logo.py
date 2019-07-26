'''
Problem :
You are given a binary matrix of size N x N which represents the pixels of a logo,
Return true or false if the logo is symmetric about both X-axis and Y-axis

Problem source: https://bit.ly/32TR0lA
'''

def is_x_symmetric(left_matrix, right_matrix):
    
    for index in range(len(left_matrix)):
        if left_matrix[index] != right_matrix[index][::-1]:
            return False

    return True

def is_y_symmetric(upper_matrix, lower_matrix):

    count = len(lower_matrix) - 1
    for index in range(len(upper_matrix)):
        if upper_matrix[index] != lower_matrix[count][::-1]:
            return False
        count -= 1
    return True

def is_symmetric(matrix):

    size = len(matrix)
    left_sub_matrix = []
    right_sub_matrix = []
    upper_sub_matrix = matrix[:size/2]
    lower_sub_matrix = matrix[size/2+1:]

    for arr in matrix:

        left_sub_matrix.append(arr[:size/2])
        right_sub_matrix.append(arr[(size/2+1):])

    return is_y_symmetric(upper_sub_matrix, lower_sub_matrix) and is_x_symmetric(left_sub_matrix, right_sub_matrix)

def main():
    
    matrix = [[0,1,1,1,0], [0,1,0,1,0], [1,0,0,0,1], [0,1,0,1,0], [0,1,1,1,0]]
    is_symmetric(matrix)

if __name__ == "__main__":
    main()