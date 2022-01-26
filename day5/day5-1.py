# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# Rich Whiffen - 1/25/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 5 - assignment 5.1 - Average height
# working with loops - they've already converted them to INT for us
count = 0 # start out at zero
total_sum = 0
for n in student_heights:
    total_sum+=student_heights[count]
    count+=1
height_average = round(total_sum / count)

#print(f"Average is {height_average}")
print(f"{height_average}")   
