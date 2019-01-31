
#O(n)^2
def compute(arr):

    return_list = []
    arr_size = len(arr)

    for i in range(arr_size):
        temp_prod = 1
        for j in range(arr_size):
            if j != i:
                temp_prod *= arr[j]
        return_list.append(temp_prod)

    return return_list


def main():
    arr = [1,2,3,4]
    print(compute(arr))

if __name__ == "__main__":
    main()
