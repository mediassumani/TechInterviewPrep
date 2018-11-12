def filter(string):
    """Returns a dupliacate-free filtered string """

    filtered_string = ""
    for char in string:
        if char not in filtered_string:
            filtered_string += char

    return filtered_string

def merge_the_tools(string,k):
    # slices the string into k different elements
    t_1 = [string[char:char+k] for char in range(0, len(string),k)]
    t_0 = []

    for subsequence in t_1:
        #filteres out duplicates from each subsequence
        current_filtered_word = filter(subsequence)
        print(current_filtered_word)

    return t_0

def main():
    s = "AABCAAADA"
    k = 3
    merge_the_tools(s,k)

if __name__ == "__main__":
    main()
