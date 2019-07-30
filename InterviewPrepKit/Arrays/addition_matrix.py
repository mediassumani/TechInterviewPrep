def sum_matrix(matrix):
    
    total_sum = 0
    for sub_arr in matrix:
        for elem in sub_arr:
            total_sum += elem

    return total_sum

def main():
    
    matrix = [
        [4, 4],
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    print(sum_matrix(matrix))
    
if __name__ == "__main__":
    main()