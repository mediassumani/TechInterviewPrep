import itertools
import sys

def compress_string_groupby(s):
    ''' Return each character of S with its occurence in a tuple using Itertools' Groupby()'''

    result = ""
    keys = []
    groups = []
    sorted_string = sorted(s)

    for key, group in itertools.groupby(s):
        keys.append(key)
        groups.append(list(group))

    for index, element in enumerate(groups):
        result += "({}, {}) ".format(len(element), element[0])

    return result


def main():

    # string_one = sys.stdin.readline()
    # compressed_string = compress_string_groupby(string_one)

    s_1 = "122231144"
    print(compress_string_groupby(s_1))



if __name__ == '__main__':
    main()
