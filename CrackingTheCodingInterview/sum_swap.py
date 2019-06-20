'''
    Given two arrays, find a pair of value(one from each array) that you can swap
    to give the two arrays the same sum

    input : [4,1,2,1,1,2] sum = 11  & [3,6,3,3] = 15
            [4,3,2,1,1,2] sum = 13  & [1,6,3,3] = 13



    output : {1,3}


    Solution 1 - Brute force

    # For each element in list A
        # Swap it with each element in list B
        # Check if sum of both alternate array is the same
'''


def sum_swap(arr_one,arr_two):

    for outter_index in range(len(arr_one)):

        for inner_index in range(len(arr_two)):
            
            # Alternate arrays
            alt_arr_one = arr_one
            alt_arr_two = arr_two

            # Swap the values
            temp_val = arr_one[outter_index]
            alt_arr_one[outter_index] = arr_two[inner_index]
            alt_arr_two[inner_index] = temp_val
            
            if sum(alt_arr_one) == sum(alt_arr_two):
                print(alt_arr_one[outter_index], alt_arr_two[inner_index])
                break
            
            # Check if same sum
            # if (sum(alt_arr_one) == sum(alt_arr_two)):
            #     print(alt_arr_one, alt_arr_two)

                # print(alt_arr_one[outter_index], alt_arr_two[inner_index])


def main():
    arr_one = [4,1,2,1,1,2]
    arr_two = [3,6,3,3]
    sum_swap(arr_one, arr_two)

if __name__ ==  "__main__":
    main()