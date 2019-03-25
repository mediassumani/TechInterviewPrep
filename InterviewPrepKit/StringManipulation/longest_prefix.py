# create prefix variable
# traverse first time on array
# set a temp prefix to first elemnt letter
# check if item at i is equalto temp preffix
    # if yes
        # append to prefix var
    # if no return preffix

def longest_prefix(strs):

        prefix = ""

        # edge case 1 - check if the string s has diff frist characters

        
        # edge case 2 - check if array is empty
        if len(strs) <= 1:
            return prefix

        for innerIndex,innerValue in enumerate(strs):
            
            if innerValue == "":
                continue
            
            temp_prefix = innerValue[innerIndex]
            for index,value in enumerate(strs):
                temp_val = value[innerIndex]
                if  temp_val == temp_prefix and temp_val not in prefix:
                    prefix += temp_val
                else:
                    break


        return prefix


def main():

    arr_one = ["flower", "flow", "flight"]
    arr_two = ["dog","racecar","car"]
    arr_three = [""]
    print(longest_prefix(arr_three))

if __name__ == "__main__":
    main()