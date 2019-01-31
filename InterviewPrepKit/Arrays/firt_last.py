def find_first_last(arr, target):

    target_indexes = []
    for i in range(len(arr)):
        if arr[i] == target:
            target_indexes.append(i)

    if len(target_indexes) == 0:
        return [-1, -1]


    first = target_indexes[0]
    last = target_indexes[len(target_indexes)-1]
    return [first, last]

def main():
    nums = [5,7,7,8,8,10]
    target = 8

    print(find_first_last(nums, target))

if __name__ == "__main__":
    main()
