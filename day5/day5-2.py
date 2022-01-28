# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# Rich Whiffen - 1/25/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# day 5 assignment 5.2 max student score from a list

# not supposed to use the max() function do it by hand to learn

max_score = 0

for score in student_scores:
    if max_score < score:
        max_score = score

print(f"The highest score in the class is: {max_score}")
