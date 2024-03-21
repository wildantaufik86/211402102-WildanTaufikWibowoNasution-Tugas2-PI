# In this second part of the first programming assignment, you should write a program that reads in numbers until a -1 is entered and prints the sum of all numbers entered in decimal format with two digits after the decimal. For example, if the user enters 5000 10 15 -1 the program should display 5025.00 (Each number will be separated by a carriage return).


# Initialize sum
total = 0

# Read numbers until -1 is entered
while True:
    num = input("Enter a number (or -1 to finish): ")
    if num == '-1':
        break
    total += float(num)

# Print the sum with two decimal places
print("{:.2f}".format(total))
