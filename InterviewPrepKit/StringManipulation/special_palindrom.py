def is_same_chars(substring):
    print(substring)
    first_elem = substring[0]
    middle_index = int((0+len(substring))/2)

    if substring[middle_index] != first_elem:
        print(substring, "same middle")
        return True

    for index in range(len(substring)):
        if substring[index] != first_elem:
            return False

    return True

def substrCount(n, s):

    arr = []
    for i in range(n):
        # add current char
        arr.append(s[i])
        # get a substring
        substring = s[:n-i]
        if is_same_chars(substring):
            arr.append(substring)

    return len(arr)




def main():

    string = "asasd"
    print(substrCount(len(string), string))


if __name__ == "__main__":
    main()
