"""
A triangle can be classified based on the lengths of its sides as equilateral, isosceles or
scalene.
    - An equilateral triangle has all three sides of the same length.
    - An isosceles triangle has two sides that are the same length, and a third side that is different.
    - A scalene triangle has all sides of different lengths.

Write a program that reads the lengths of the three sides of a triangle from the
user. Ensure that the inputs form a valid triangle before determining the type.
"""

# Read the lengths of the three sides from the user
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check if the inputs form a valid triangle
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    # Determine the type of triangle
    if side1 == side2 == side3:
        print("The triangle is equilateral.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
else:
    print("The given lengths do not form a valid triangle.")
