
# Time : O(n)^2
# Space : O(1) -> constant space
def compute(arr):

    return_list = []
    arr_size = len(arr)

    # checks if the array is empty or with 1 element
    if len(arr) <= 1:
        return arr

    for i in range(arr_size):
        temp_prod = 1
        for j in range(arr_size):
            if j != i:
                temp_prod *= arr[j]
        return_list.append(temp_prod)

    return return_list




def main():
    arr = [1,2,0,0]
    print(compute(arr))

if __name__ == "__main__":
    main()
