'''
Question : Given a string input of parentheses, retur true or false if they are valid.
Examples: "(())" -> True , "())" -> False , "()()()" -> True
Time : 15 minutes
Difficulty : Easy-Medium
'''

from collections import deque

def is_valid_parentheses(s):
    
    if not s or s[0] == ")":
        return False

    parenthese_type = ("(", ")")
    queue = deque([]) 
    
    for char in s:
        if char == parenthese_type[0]:
            queue.append(char)
        elif char == parenthese_type[1]:
            queue.popleft()

    if len(queue) == 0:
        return True

    return False

def main():
    
    print(is_valid_parentheses(")(())()"))

if __name__ == "__main__":
    main()

