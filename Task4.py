# Write a program that takes in grades one at a time until a -1 is seen to mark the end of the list.  Each grade will be separated by an enter key.  When you are done, output the average (as an int) followed by the grades in order that you saw them.
# An example execution would look like this:
# Input:
# 80
# 75
# 70
# -1
# Output:
# 75
# 80
# 75
# 70

# Initialize list to store grades
grades = []

# Read grades until -1 is entered
while True:
    grade = input("Enter a grade (or -1 to finish): ")
    if grade == '-1':
        break
    grades.append(int(grade))

# Calculate average
average_grade = sum(grades) // len(grades)

# Print average followed by the grades in order
print(average_grade)
for grade in grades:
    print(grade)
