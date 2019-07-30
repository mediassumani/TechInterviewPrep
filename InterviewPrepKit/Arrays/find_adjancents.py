'''
Given a 2-d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically
'''

def find_coordinates(matrix, element, n, m):
    '''
        Finds the x,y coordinates of an element in matrix given row size n, and column size m
        Time & Space Complexity : O(n*m) | O(1) -> n = # of row, m = # of cols
    '''
    for x in range(n):
        for y in range(m):
            if matrix[x][y] == element:
                return (x,y)
    return None
            
def get_adjacent(matrix, element):
    '''
        Finds and returns all the elements adjacents to a given element in a matrix
        Time & Space Complexity :  O(n*m) | O(n) O(1) -> n = # of row, m = # of cols
    '''
    
    row_size = len(matrix)
    col_size = len(matrix[0])
    adjacents = []
    x,y = find_coordinates(matrix, element, row_size, col_size)

    for row in range(row_size):
        if ((row-x) <= 1):
            for col in range(col_size):
                if ((col - y) <= 1):
                    if matrix[row][col] == element:
                        continue
                    if (abs(x-row) <= 1) and (abs(y-col) <= 1):
                        adjacents.append(matrix[row][col])
                else:
                    continue
        else:
            continue

    return adjacents

def main():
    
    matrix = [
           
        ["A","B","C","D","E"],
        ["F","G","J","K","L"],
        ["M","N","O","P","Q"],
        ["R","S","T","U","V"]
    ]
    
    print(get_adjacent(matrix, "G"))
    
if __name__ == "__main__":
    main()