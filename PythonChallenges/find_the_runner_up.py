def find_max(arr):
    max = 0
    runner_up = 0
    for num in arr:
        if num >= max:
            max = num
        if (num + 1) == max:
            runner_up = num

    return runner_up

def find_runner_up(n,arr):

    runner_up = find_max(arr)
    return runner_up


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(find_runner_up(n,arr))
