import itertools
import sys

# O(n)
def compress_string_groupby(s):
    ''' Return each character of S with its occurence in a tuple using Itertools' Groupby()'''

    result = ""
    groups = []
    # O(n)
    for key, group in itertools.groupby(s):
        result += "({}, {}) ".format(len(list(group)), list(group)[0])

    return result

def main():

    s_1 = "122231144"
    print(compress_string_groupby(s_1))

if __name__ == '__main__':
    main()
