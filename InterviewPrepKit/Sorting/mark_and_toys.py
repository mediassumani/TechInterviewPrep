def maximumToys(prices, k):

    max = 0
    num_of_possible_toys = 0
    sorted_prices = sort(prices) # O(nlog n)

    #O(n)
    for index in range(len(sorted_prices)):
        max += prices[index]
        if max <= k:
            num_of_possible_toys += 1

    return num_of_possible_toys
