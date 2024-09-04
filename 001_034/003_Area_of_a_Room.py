"""
Write a program that asks the user to enter the width and length of a room. Once
these values have been read, your program should compute and display the area of
the room. The length and the width will be entered as floating-point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with.
"""
"""
Write a program that asks the user to enter the width and length of a room. Once
these values have been read, your program should compute and display the area of
the room. The length and the width will be entered as floating-point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with.
"""
# Ask the user to enter the room width
width = float(input("Enter the room width in meters: "))

# Ask the user to enter the room length
length = float(input("Enter the room length in meters: "))

# Calculate and print the area of the room
print(f"The area of the room is: {width * length} square meters")
