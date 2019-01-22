def count_swaps(arr):

    num_of_iterations = len(arr) - 1
    swap_count = 0
    length = len(arr)
    for i in range(num_of_iterations):
        for j in range(num_of_iterations):
            if arr[j] > arr[j+1]:
                swap_count += 1
                arr[j], arr[j+1] = arr[j+1],arr[j]

    print("Array is sorted in {} swaps".format(swap_count))
    print("First Element: {} ".format(arr[0]))
    print("Last Element: {} ".format(arr[length]))
