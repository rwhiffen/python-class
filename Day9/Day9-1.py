# Rich Whiffen - 2/10/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 9 - assignment 9.1 - Student grades
# workign with python dictionaries
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
     if student_scores[student] > 90:
         student_grades[student] = "Outstanding"
     elif student_scores[student] > 80:
         student_grades[student] = "Exceeds Expectations"
     elif student_scores[student] > 70:
         student_grades[student] = "Acceptable"
     else:
         student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)
