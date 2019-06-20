def is_unique(string):
    return True

def get_long_sbtrs(string):

    sbtrs = [] # hold all the substrings

    for i, char in enumerate(string):
        outter_char = char
        for index in range(index+1, len(string)):
            curr_sbtr = string[i: index]
            if is_unique(curr_sbtr):
                sbtrs.append(curr_sbtr)

    return max(sbtrs)


