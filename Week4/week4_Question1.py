"""
# 
# File      : Question-1.py
# Created   : 10/10/2021 05:06
# Author    : M. Curley
# Version   : v1.0.0
# Licencing : (c) 2021 Michael J. Curley, LYIT
#             Available under GNU Public Licence(GPL)
# Description :
#
"""

if __name__ == '__main__':
    student_numbers = ("L12345", "L54321")
    student_modules = ["Java_Programming", "Python Scripting"]
    java_student_grades = {"L12345": 40, "L54321": 70}
    python_student_grades = {"L12345":69, "L54321": 58}

    student = (input("Please enter your student number"))
    student = str.upper(student)

    if student in student_numbers:
        java_grade = str(java_student_grades[student])
        python_grade = str(python_student_grades[student])
        print("Student " + student + " Your java grade is " + java_grade + " and your python grade is " + python_grade)
