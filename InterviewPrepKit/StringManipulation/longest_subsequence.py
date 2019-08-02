'''

Find the longest sequence of charaters that appears left-to-right(not necessarly contguous)
in both string.
'''

def solution(string_1, string_2):
    ''' 
        Naive approach by comparing each character from each string
        Time complexity : 
    '''

    result = ""
    for index_one in range(len(string_1)):
        if string_1[index_one] in string_2:
            result += string_1[index_one]
    return result

def find_long_subsequence(string_1, string_2):
    return solution(string_1, string_2)

def main():
    
    str_one = "ABAZDC"
    str_two = "BACBAD"
    print(find_long_subsequence(str_one, str_two))

if __name__ == "__main__":
    main()