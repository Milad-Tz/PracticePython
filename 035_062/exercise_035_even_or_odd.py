"""
Write a program that reads an integer from the user. Then your program should
display a message indicating whether the integer is even or odd.
"""

# Prompt the user to enter an integer
number = int(input("Enter an integer: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
