def find_high_prod(arr): # O(n^3) time | O(n) space

    high_prods = []
    size = len(arr)

    for x in range(size):
        for y in range(size):
            if y == x:
                continue
            for z in range(size):
                if z == y or z == x:
                    continue
                else:
                    prod = arr[x] * arr[y] * arr[z]
                    high_prods.append(prod)

    return max(high_prods)

def main():
    
    nums = [1,4,2,5,3]
    print(find_high_prod(nums))

if __name__ == "__main__":
    main()