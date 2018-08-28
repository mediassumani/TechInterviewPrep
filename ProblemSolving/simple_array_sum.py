# Problem #1 : Given an array of integers, find the sum of its elements.
# Category : Easy
# Time alocated : 10 - 15 minutes
# Time used : 5 minutes

def array_sum(array):
    sum = [n + n for n in array]
    return sum[len(sum) - 1]

def main():
    list = [1,2,3]
    print(array_sum(list))

if __name__ == '__main__':
    main()
