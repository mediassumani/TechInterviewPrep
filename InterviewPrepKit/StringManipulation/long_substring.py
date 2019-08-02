def is_unique(string):
    
    histogram = {}
    for char in string:
        if char not in histogram:
            histogram[char] = 1
        else:
            return False
    return True

def get_long_sbtrs(string):
    ''' Finds the longest unique substring in a given string'''

    sbtrs = [] # hold all the substrings

    for i, char in enumerate(string):
        for index in range(i+1, len(string)):
            curr_sbtr = string[i: index+1]
            if is_unique(curr_sbtr):
                sbtrs.append(curr_sbtr)

    return max(sbtrs, key=len)

def main():
    
    word = "abccdef"
    print(get_long_sbtrs(word))

if __name__ == "__main__":
    main()

