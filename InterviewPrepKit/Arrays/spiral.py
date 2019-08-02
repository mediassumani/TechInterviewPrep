

def spiral(matrix):
    
    R = len(matrix)
    C = len(matrix[0])
    result = []
    seen = {} # keep track of seen elements, key = position, value = elem

    # Get elements on first row
    result += matrix[0]
    row = col = 0

    while row <= R:
        while col <= C:
            
            elem = matrix[row][col]
            position = (row, col)

            if position not in seen:
                result.append(elem)
                col += 1

        col = C - 1
        row += 1
    print(result)

            


def main():
    matrix = [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ],
        [ 8, 0, 3 ]
    ]

    ''' 1 2 3 6 9 3 0 8 7 4 5 8 7'''

    spiral(matrix)


if __name__ == "__main__":
    main()