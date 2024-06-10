'''
 FormaServe IBM i Training

 For full disclaimer see https://www.formaserve.co.uk/examples.php

 © - FormaServe Systems Ltd.  1990 - 2024

 www.FormaServe.co.uk
 powerwire.eu

*** NOT FOR PUBLIC VIEWING ***

'''

student_grades = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'Diana': 95
}

# Adding 'Eve' with a grade of 88
student_grades['Eve'] = 88
print(student_grades)


# Calculating the average grade
total_grades = sum(student_grades.values())
number_of_students = len(student_grades)
average_grade = total_grades / number_of_students

print(f"The average grade is: {average_grade:.2f}")
