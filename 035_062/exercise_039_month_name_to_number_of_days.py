"""
The length of a month varies from 28 to 31 days. In this exercise, you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display “28 or 29 days”
for February so that leap years are addressed.
"""

# Prompt the user to enter the name of the month
month = input("Enter the name of a month: ").capitalize()

# Determine the number of days in the month
if month in ("January", "March", "May", "July", "August", "October", "December"):
    days = "31 days"
elif month in ("April", "June", "September", "November"):
    days = "30 days"
elif month == "February":
    days = "28 or 29 days"
else:
    days = None

# Display the result
if days:
    print(f"{month} has {days}.")
else:
    print("Error: Please enter a valid month name.")
