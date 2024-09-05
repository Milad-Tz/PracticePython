"""
The surface of the Earth is curved, and the distance between degrees of longitude
varies with latitude. As a result, calculating the distance between two points on the
Earth’s surface requires more than just using the Pythagorean theorem.

Given the latitude (t1, t2) and longitude (g1, g2) of two points, the formula to compute
the great-circle distance between them, following the surface of the Earth, is:

distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))

Where 6371.01 is the average radius of the Earth in kilometers.

Your task is to create a program that takes the latitude and longitude of two points on
Earth in degrees, converts these values into radians, and calculates the distance between
the two points using the formula provided.

Hint: Python’s trigonometric functions work with radians, so you will need to convert
degrees to radians before performing calculations. You can use the radians() function
from Python's math module to convert degrees to radians.
"""

import math  # Import math module for trigonometric functions and conversions

# Constant for Earth's average radius in kilometers
EARTH_RADIUS_KM = 6371.01

# Prompt the user to enter the latitude and longitude of the first point in degrees
t1 = float(input("Enter the latitude of the first point (in degrees): "))
g1 = float(input("Enter the longitude of the first point (in degrees): "))

# Prompt the user to enter the latitude and longitude of the second point in degrees
t2 = float(input("Enter the latitude of the second point (in degrees): "))
g2 = float(input("Enter the longitude of the second point (in degrees): "))

# Convert the input values from degrees to radians
t1 = math.radians(t1)
g1 = math.radians(g1)
t2 = math.radians(t2)
g2 = math.radians(g2)

# Calculate the distance between the two points using the spherical distance formula
distance = EARTH_RADIUS_KM * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))

# Display the calculated distance in kilometers, rounded to 2 decimal places
print(f"The distance between the two points is: {distance:.2f} kilometers")
