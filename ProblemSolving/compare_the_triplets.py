
#Problem : comparison between two arrays
# Category : Easy
# Time allocated : 15 minutes
# Time used : 17 minutes

def comparison(first_scores, second_scores):
    a_score = 0
    b_score = 0
    final_scores = []
    assert(len(first_scores) == len(second_scores))
    for index in range(len(first_scores)):
        if first_scores[index] > second_scores[index]:
            a_score += 1
        elif first_scores[index] < second_scores[index]:
            b_score += 1
        else:
            continue

    final_scores.append(a_score)
    final_scores.append(b_score)
    return final_scores

def main():

    a = [17,28,30]
    b = [99,16,8]

    print(comparison(a,b))


if __name__ == '__main__':
    main()
