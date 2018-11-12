"""
Consider the following:

A string, , of length  where .
An integer, , where  is a factor of .
We can split  into  subsegments where each subsegment, , consists of a contiguous block of  characters in .
 Then, use each  to create string  such that:

The characters in  are a subsequence of the characters in .
Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once. In other words, if the character at some index  in  occurs at a previous index  in , then do not include the character in string .
Given  and , print  lines where each line  denotes string .

"""


def merge_the_tools(string,k):

    t_1 = [string[char:char+k] for char in range(0, len(string),k)]
    t_0 = []

    for index, word in enumerate(t_1):
        for char in word:
            if word.count(char) == 1:
                print(char)



def main():
    s = "AABCAAADA"
    k = 3
    merge_the_tools(s,k)


if __name__ == "__main__":
    main()
