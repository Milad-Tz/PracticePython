"""
In the previous exercise you created a program that computed the area of a triangle
when the length of its base and its height were known. It is also possible to compute
the area of a triangle when the lengths of all three sides are known. Let s1, s2, and s3
be the lengths of the sides. Let s = (s1 + s2 + s3)/2. Then the area of the triangle
can be calculated using the following formula:

    area = sqrt(s × (s − s1) × (s − s2) × (s − s3))

Develop a program that reads the lengths of the sides of a triangle from the user and
displays its area.
"""

import math  # Import math module for square root function

# User input for the lengths of the three sides
s1 = float(input("Enter the length of the first side (s1): "))
s2 = float(input("Enter the length of the second side (s2): "))
s3 = float(input("Enter the length of the third side (s3): "))

# Compute the semi-perimeter (s)
s = (s1 + s2 + s3) / 2

# Compute the area using the formula
area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

# Display the result
print(f"The area of the triangle is {area:.2f} square units.")
