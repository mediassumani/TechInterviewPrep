
#Problem : comparison between two arrays
# Category : Easy
# Time allocated : 15 minutes
# Time used : 17 minutes

def comparison(first_scores, second_scores):

    final_scores = [0,0] # index 0 is for a and index 1 is for b
    assert(len(first_scores) == len(second_scores))
    for index in range(len(first_scores)):
        if first_scores[index] > second_scores[index]:
            final_scores[0] += 1
        elif first_scores[index] < second_scores[index]:
            final_scores[len(final_scores) - 1] += 1
        else:
            continue
    return final_scores

def main():

    a = [17,28,30]
    b = [99,16,8]

    print(comparison(a,b))


if __name__ == '__main__':
    main()
