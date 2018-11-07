
"""
there are  5 students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

"""

def find_second_lowest_score(arr):
    scores = []
    sorted_list = sorted(arr)
    for student in arr:
        scores.append(student[1])

    sorted_scores = sorted(scores)
    second_lowest = sorted_scores[1]

    for student in sorted_list:
        if student[1] is second_lowest:
            print(student[0])



def main():
    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
    find_second_lowest_score(students)



if __name__ == "__main__":
    main()
