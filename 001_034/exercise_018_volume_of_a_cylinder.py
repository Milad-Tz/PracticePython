"""
The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal place.
"""
import math  # Import math module to use the constant pi

# Prompt the user to enter the radius of the cylinder's base
radius = float(input("Enter the radius of the cylinder's base (in units): "))

# Prompt the user to enter the height of the cylinder
height = float(input("Enter the height of the cylinder (in units): "))

# Calculate the volume of the cylinder using the formula: volume = π * r^2 * h
volume = math.pi * radius ** 2 * height

# Display the result rounded to one decimal place
print(f"The volume of the cylinder is: {volume:.1f} cubic units.")
