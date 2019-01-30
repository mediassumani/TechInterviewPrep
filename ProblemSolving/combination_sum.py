from itertools import combinations

def combine(arr, target):
    ''' my attempted solution lol'''

    solution_set = []
    temp_array = []
    arr_size = len(arr)

    for i in arr:
        for j in arr:
            curr_sum = i + j
            if curr_sum <= target:
                if curr_sum == target:
                    target_list = [i,j]
                    solution_set.append(sorted(target_list))
                elif curr_sum < target:
                    # traverse temp to see if there's an element we can use there
                    for num in temp_array:
                        if num + curr_sum == target:
                            if sorted([inner_curr, outter_curr, num]) not in solution_set:
                                solution_set.append(sorted([inner_curr, outter_curr, num]))

    return solution_set

def combine_solution(arr, target, partials=[]):
    ''' from stack overflow lol'''

    # base case
    s = sum(partials)
    if s == target:
        print "sum(%s)=%s" % (partials, target)
    if s >= target:
        return

    # recursive
    for index in range(len(arr)):
        curr = arr[index]
        remaining = arr[index+1:]
        combine_solution(remaining, target, partials + [curr])

def main():

    arr = [2,3,5,2]
    target = 7
    print(combine_solution(arr, target))

if __name__ == "__main__":
    main()
