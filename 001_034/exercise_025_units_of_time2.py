"""
In this exercise, you will reverse the process described in Exercise 24.
Develop a program that begins by reading a number of seconds from the user.
Then your program should display the equivalent amount of time in the form D:HH:MM:SS,
where D, HH, MM, and SS represent days, hours, minutes, and seconds, respectively.
The hours, minutes, and seconds should all be formatted to exactly two digits
with leading zeros.
"""

# Read the number of seconds from the user
total_seconds = int(input("Enter the number of seconds: "))

# Calculate the number of days, hours, minutes, and seconds
days = total_seconds // (24 * 3600)
total_seconds = total_seconds % (24 * 3600)
hours = total_seconds // 3600
total_seconds = total_seconds % 3600
minutes = total_seconds // 60
seconds = total_seconds % 60

# Display the result in D:HH:MM:SS format with leading zeros for hours, minutes, and seconds
print(f"{days}:{hours:02}:{minutes:02}:{seconds:02}")
