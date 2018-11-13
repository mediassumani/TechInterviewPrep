def compute_happiness(array, set_one, set_two, n, m):
    """Returns the happiness level based on two sets and array """

    happiness_level = 0
    for integer in array:
        if integer in set_one:
            happiness_level +=1
        elif integer in set_two:
            happiness_level -= 1

    return happiness_level

def main():

    array = [1,5,7,6]
    A = [3,1]
    B = [5,7,6]

    print(compute_happiness(array,A,B,3,2))

if __name__ == '__main__':
    main()
