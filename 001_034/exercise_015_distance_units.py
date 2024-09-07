"""
In this exercise, you will create a program that begins by reading a measurement
in feet from the user. Then your program should display the equivalent distance in
inches, yards and miles. Use the Internet to look up the necessary conversion factors
if you don’t have them memorized.
"""
# Define conversion factors
INCHES_PER_FOOT = 12
YARDS_PER_FOOT = 1 / 3  # 1 yard is 3 feet, so 1 foot is 1/3 yard
MILES_PER_FOOT = 1 / 5280  # 1 mile is 5280 feet

# Prompt the user to enter the measurement in feet
feet = float(input("Enter the distance in feet: "))

# Convert feet to inches, yards, and miles
inches = feet * INCHES_PER_FOOT
yards = feet * YARDS_PER_FOOT
miles = feet * MILES_PER_FOOT

# Display the results
print(f"The equivalent distance is:")
print(f"{inches:.2f} inches")
print(f"{yards:.2f} yards")
print(f"{miles:.6f} miles")
