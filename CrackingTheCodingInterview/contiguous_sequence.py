'''
You are given an array of integers(positive and negative), Find the contiguous 
sequence with the largest sum. Return the sum
'''

def find_largest_seq(numbers):
    # O(n^2) time | O(n) space
    if not numbers:
        return None
    
    sum_array = []
    arr_size = len(numbers)

    for index in range(arr_size):
        
        curr_seq = numbers[index: arr_size]
        curr_sum = sum(curr_seq)
        sum_array.append(curr_sum)

    return max(sum_array)


def main():

    nums = [2,-3,-1,5,1]
    print(find_largest_seq(nums))

if __name__ == "__main__":
    main()

# Solution 1 - O(n^2) time and O(n) space

# Create an array of sums - O(n) space
# Traverse through the array from i to length of array - O(n) time
# Grab all the element in range of i to length of array - O(n) space, O(1) time
    # sum up all the elements in that subsequenece range # O(n) space

    # append the sum in the list of sums

# Find the maximum element in sums array
