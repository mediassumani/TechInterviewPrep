
# Challenge Name : Integers Come In All Sizes
# Programmer : Medi Assumani
# Task : Read four numbers, a,b,c,d, and print the result of a^b + c^d


        # Function to compute te exponentiation
import sys

def exponent(base,power):
    count = 1
    result = base
    if power == 0:
        return 1
    elif power == count:
        return base
    else:
        while count < power:
            result = result * base
            count += count

    return result

    # Function to compute the task
def compute_answer(one,two,three,four):
    result = exponent(one,two) + exponent(three,four)
    return result

        # The data from the user
num_one = raw_input("Enter the first number : ")
num_two = raw_input("Enter the second number : ")
num_three = raw_input("Enter the third number : ")
num_four = raw_input("Enter the fourth number : ")

final_answer = compute_answer(int(num_one),int(num_two),int(num_three),int(num_four))
print final_answer
