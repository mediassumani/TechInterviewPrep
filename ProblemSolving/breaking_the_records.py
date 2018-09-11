'''

Complete the breakingRecords function in the editor below.
It must return an integer array containing the numbers oftimes she broke her records


Category : Easy
Allocated time : 15 minutes
Time used :

'''
def breakingRecords(array_of_scores):

    min = array_of_scores[0]
    max = array_of_scores[0]
    score_increment = 0
    score_decrement = 0

    for score in range(len(array_of_scores)):
        temp = array_of_scores[score]
        if temp > max:
            max = temp
            score_increment += 1

        elif temp < max:
            min = temp
            score_decrement += 1

        else:
            continue

    return (score_increment, score_decrement)


def main():

    test_one = [10,5,20,20,4,5,2,25,1]
    print(breakingRecords(test_one))


if __name__ == '__main__':
    main()
