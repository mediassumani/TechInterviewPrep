'''
    Given an array of strings, group anagrams together
'''

def is_same_letters(str_1, str_2):
    
    for char in str_1:
        if char not in str_2:
            return False

    return True

def group_anagrams(array):

    anagrams = []
    
    for outter_word in array:
        temp_arr = [outter_word]

        for inner_word in array:
            if outter_word != inner_word:
                if is_same_letters(outter_word, inner_word):
                    temp_arr.append(inner_word)

        anagrams.append(temp_arr)
    return anagrams


def main():

    arr = ["eat", "nat", "tea", "tan", "bat"]
    group_anagrams(arr)


if __name__ == "__main__":
    main()