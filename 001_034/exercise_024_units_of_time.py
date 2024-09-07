"""
Create a program that reads a duration from the user as a number of days, hours,
minutes, and seconds. Compute and display the total number of seconds represented
by this duration.
"""

# User input for days, hours, minutes, and seconds
days = int(input("Enter the number of days: "))
hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))

# Compute the total number of seconds
total_seconds = (days * 24 * 3600) + (hours * 3600) + (minutes * 60) + seconds

# Display the result
print(f"The total number of seconds is: {total_seconds}")
