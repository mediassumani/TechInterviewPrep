"""
PROBLEM:
    - Given a string, find the length of the longest substring without repeating characters.
    Time allocated : 20 minutes
    Time used : 1 hour
    Time Complexity :
        - Worst Case : O(n) if we have to trasverse s at its entirerity
        - Best Case : O(1) if the length of s is 0
"""


def lengthOfLongestSubstring(s):

    list_of_substrings = []
    string = ""

    if len(s) == 0:
        return 0

    for index in range(len(s)):

        string += s[index]
        next_character = s[index+1:index+2]
        if next_character in string:
            list_of_substrings.append(len(string))
            string = ""

    if len(list_of_substrings) != 0:
        return max(list_of_substrings)

    else:
        return 1


def main():

    # print(lengthOfLongestSubstring("au"))
    # print(lengthOfLongestSubstring("abcabcbb"))
    # print(lengthOfLongestSubstring("bbbbb"))
    # print(lengthOfLongestSubstring("pwwkew"))
    print(lengthOfLongestSubstring(""))

if __name__ == "__main__":
    main()
