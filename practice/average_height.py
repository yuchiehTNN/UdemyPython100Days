# goal is to not using sum and len function

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
count = 0
total = 0
for height in student_heights:
    count += 1
    total += height

print(count, round(total / 5))
