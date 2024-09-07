"""
Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.
Hint: One foot is 12 inches. One inch is 2.54 centimeters.
"""
# Define conversion factors
INCHES_PER_FOOT = 12
CM_PER_INCH = 2.54

# Prompt the user to enter the height in feet and inches
feet = int(input("Enter the number of feet: "))
inches = int(input("Enter the number of inches: "))

# Convert the height to total inches
total_inches = (feet * INCHES_PER_FOOT) + inches

# Convert total inches to centimeters
centimeters = total_inches * CM_PER_INCH

# Display the result
print(f"The height is {centimeters:.2f} centimeters.")
