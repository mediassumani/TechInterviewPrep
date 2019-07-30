def print_even(matrix):
    
    for sub_arr in matrix:
        print([elem for elem in sub_arr if elem % 2 == 0])

def main():
    
    matrix = [
        [2,3,21,16],
        [9,18,6],
        [4,5,10,13]
    ]
    print_even(matrix)
    
if __name__ == "__main__":
    main()