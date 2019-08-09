
def find_zero_positions(matrix):

    positions = []
    row_length = len(matrix)
    col_length = len(matrix[0])

    for row in range(row_length):
        for col in range(col_length):
            if matrix[row][col] == 0:
                coordinate = (row, col)
                positions.append(coordinate)
    return positions

def change_values(matrix):

    positions = set(find_zero_positions(matrix))
    row_length = len(matrix)
    col_length = len(matrix[0])
    cols = set([tup[1] for tup in positions])

    for row in range(row_length):
        for col in range(col_length):
            curr_pos = (row, col)
            # Swapping columns
            if col in cols:
                matrix[row][col] = 0
            if curr_pos in positions:
                # Swapping row
                matrix[row] = [0 for i in range(row_length)]

    return matrix
                
def main():
    
    matrix = [
        [1,1,0,1,1],
        [1,1,1,1,1],
        [1,1,1,0,1],
        [1,1,1,1,1],
        [0,1,1,1,1],
    ]
    change_values(matrix)

if __name__ == "__main__":
    main()