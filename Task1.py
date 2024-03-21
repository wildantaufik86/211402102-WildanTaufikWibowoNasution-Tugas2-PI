# Write a program that reads in a number and prints the date that number of days from now in this format: Saturday, February 06, 2021.


from datetime import datetime, timedelta
# Read number of days from user input
num_days = int(input("Enter number of days: "))
# Calculate future date
future_date = datetime.now() + timedelta(days=num_days)
# Print future date in the specified format
print(future_date.strftime("%A, %B %d, %Y"))
