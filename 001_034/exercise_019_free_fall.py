"""
This program calculates the final speed of an object when it hits the ground after being dropped from a certain height.
The user will input the height in meters (m) from which the object is dropped.
The initial speed (vi) is assumed to be 0 m/s since the object is dropped from rest.
The acceleration due to gravity (a) is taken as 9.8 m/s².
The final speed (vf) can be calculated using the kinematic equation:

    vf = sqrt(vi² + 2 * a * d)

where:
    - vi is the initial speed (0 m/s in this case),
    - a is the acceleration due to gravity (9.8 m/s²),
    - d is the distance (height in meters).

Note:
    - Python’s `math` module is used to perform the square root operation.
    - Ensure that the input height is a non-negative value.
"""
import math  # Import math module to use the square root function

# Define the acceleration due to gravity in m/s²
GRAVITY = 9.8  # m/s²

# Prompt the user to enter the height from which the object is dropped
height = float(input("Enter the height from which the object is dropped (in meters): "))

# Calculate the final speed using the formula: vf = sqrt(vi² + 2 * a * d)
# Since vi (initial velocity) is 0, the formula simplifies to vf = sqrt(2 * a * d)
final_speed = math.sqrt(2 * GRAVITY * height)

# Display the final speed rounded to two decimal places
print(f"The final speed of the object when it hits the ground is {final_speed:.2f} m/s.")
