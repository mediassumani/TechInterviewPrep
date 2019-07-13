# Problem reference : https://www.geeksforgeeks.org/print-all-the-super-diagonal-elements-of-the-given-square-matrix/

def find_diagonal_elements(matrix):
    # O(n) where n is the length of the matrix
    diagonal_list = []
    row = 0
    col = 1
    while col < len(matrix):
        diagonal_list.append(matrix[row][col])
        row += 1
        col += 1

    return diagonal_list

def main():
    
    matrix = [
        [1, 2, 3, 4],
        [3, 3, 4, 4],
        [2, 4, 6, 3],
        [1, 1, 1, 3]
    ]

    print(find_diagonal_elements(matrix))
if __name__ == "__main__":
    main()