def filter_array(array):

    filtered_array = []
    for integer in array:
        if integer not in filtered_array:
            filtered_array.append(integer)

    return filtered_array

def compute_happiness(array, set_one, set_two, n, m):

    happiness_level = 0
    filtered_array = filter_array(array)
    for integer in filtered_array:
        if integer in set_one:
            happiness_level +=1
        elif integer in set_two:
            happiness_level -= 1

    return happiness_level

def main():

    array = [1,5,3]
    A = [3,1]
    B = [5,7]

    print(compute_happiness(array,A,B,3,2))


if __name__ == '__main__':
    main()
