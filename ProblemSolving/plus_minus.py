''' Problem # 5 :
Given an array of integers,
calculate the fractions of its elements that are positive,
negative, and are zeros. Print the decimal value of each fraction on a new line.


 Category : Easy
 Allocated time : 15 minutes
 Time used : 18 minutes

'''

from decimal import Decimal

def plus_minus(arr):

        #NEEDED VARIABLES
    arr_length = Decimal(len(arr))
    num_of_positives = 0
    num_of_negatives = 0
    num_of_zeroes = 0

        #LOOPING THROUGH ARRAY
    for index in arr:
        if index > 0 :
            num_of_positives += 1
        elif index < 0 :
            num_of_negatives += 1
        else:
            num_of_zeroes += 1

    return (format((num_of_positives/arr_length), '.6f'),format((num_of_negatives/arr_length), '.6f'), format((num_of_zeroes/arr_length), '.6f'))

def main():
    arr = [1,1,0,-1,-1]
    print(plus_minus(arr))


if __name__ == '__main__':
    main()
