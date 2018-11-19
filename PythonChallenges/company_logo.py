'''
Given a string , which is the company name in lowercase letters,
 your task is to find the top three most common characters in the string
'''
def common_chars(company_name):
    dict_of_chars = {}
    top_occur = 0

    for character in company_name:
        if character not in dict_of_chars:
            occurence = company_name.count(character)
            dict_of_chars[character] = occurence

def main():
    common_chars('aabbbccde')

if __name__ == "__main__":
    main()
