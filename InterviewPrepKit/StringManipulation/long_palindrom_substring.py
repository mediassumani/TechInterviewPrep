def is_palindrome(string): 
    return string == string[::-1]
    
def find_max( arr):
    max_str = arr[0]
    for string in arr:
        
        if len(string) > len(max_str):
            max_str = string
    return max_str
            
    
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    
    if len(s) == 0:
        return ""
    
    elif len(s) == 1:
        return s
    
    substrings = []
    
    for x in range(len(s)):
        for y in range(len(s)):
            
            curr_sub = s[x:y+1]
            
            if curr_sub:
                if is_palindrome(curr_sub):
                    substrings.append(str(curr_sub))
    
    if len(substrings) != 0:
        return find_max(substrings)
    
    return None