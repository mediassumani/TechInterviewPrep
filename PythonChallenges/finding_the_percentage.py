from decimal import Decimal

"""
You have a record of  students. Each record contains the student's name,
and their percent marks in Maths, Physics and Chemistry. The marks can be floating values.
The user enters some integer  followed by the names and marks for students. You are required
to save the record in a dictionary data type. The user then enters a student's name. Output the
average percentage marks obtained by that student, correct to two decimal places.
"""

def find_percentage(num_of_students, student_marks, student_name):
    """  Returns the percentage of the student
    @params:
     _ num_of_students : the total amount of students
     _ student_marks : a dictionary containing the student names -> their marks on courses
     _ student_name : The student in which we are looking his/her avg percentage

     @return
        _ avg_percentage:  The average percentage mark
    """

    list_size = len(student_marks[student_name])
    avg_percentage = sum(student_marks[student_name]) / list_size

    return format(avg_percentage, '.2f')

def main():

    marks = {"Harsh": [25,26.5,28], "Anurag": [26,28,30]}
    print(find_percentage(len(marks),marks, "Harsh"))


if __name__ == "__main__":
    main()
