"""

Given the participants' score sheet for your University Sports Day, you are
required to find the runner-up score. You are given scores. Store them in a
list and find the score of the runner-up.

"""
def find_runner_up(arr,n):
    counter = n
    sorted_list = sorted(arr)
    while counter > 0:
        if sorted_list[counter - 2] != sorted_list[counter - 1]:
            return sorted_list[counter - 2]
        else:
            counter -= 1
    return counter
