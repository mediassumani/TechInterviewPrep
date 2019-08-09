'''
Quesion from : https://www.interviewcake.com/question/python/find-rotation-point
Write a function for finding the index of the "rotation point,"
which is where I started working from the beginning of the dictionary.
'''

def find_rotation_point(word_list): # O(n) time | O(1) space

    prev_word = None
    rotation_index = None

    for index,word in enumerate(word_list):
        if prev_word:
            if word < prev_word:
                rotation_index = index
                break
        prev_word = word
    return rotation_index

def main():
    
    words = [
        'ptolemaic',
        'retrograde',
        'supplant',
        'undulate',
        'xenoepist',
        'xolo',
        'xzubu',
        'zaver',
        'zulu',
        'asymptote',  # <-- rotates here!
        'babka',
        'banoffee',
        'engender',
        'karpatka',
        'othellolagkage',
    ]

    find_rotation_point(words)

if __name__ == "__main__":
    main()