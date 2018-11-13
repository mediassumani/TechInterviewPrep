"""
Given a list of duplicates numbers with 1 unique number,
return that unique numberself.
"""
def unique_digit(list):
    for digit in list:
        count = list.count(digit)
        if count == 1:
            return digit

def main():
    list = [5,10,10,77,77]
    print(unique_digit(list))

if __name__ == "__main__":
    main()
