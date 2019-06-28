# Given -> Array
# Return -> K largest values
# Assumptions : 
    #  K can be > len(arr),
    #  Ignore Duplicates, return first seen
    #  arr contains +,- integers and doubles
    # We can sort array for now

def find_k_largest(arr, k):
    
    k_largests = []
    if k > len(arr) or len(arr) == 0:
        return None

    sorted_arr = sorted(arr, reverse=True)
    counter = 0
    hist = {}

    while counter <= k:

        curr_val = sorted_arr[counter]
        if curr_val not in hist:
            k_largests.append(curr_val)
            hist[curr_val] = "seen"
        counter += 1

    return k_largests

def main():
    
    arr = [3,3,7,3,-9]
    k = 3
    print(find_k_largest(arr, k))

if __name__ == "__main__":
    main()