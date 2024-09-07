import math  # Import math module to use the constant pi

# Prompt the user to enter the radius
radius = float(input("Enter the radius (r): "))

# Calculate the area of the circle using the formula: area = π * r^2
area_of_circle = math.pi * radius ** 2

# Calculate the volume of the sphere using the formula: volume = 4/3 * π * r^3
volume_of_sphere = (4 / 3) * math.pi * radius ** 3

# Display the results
print(f"The area of the circle with radius {radius} is: {area_of_circle:.2f}")
print(f"The volume of the sphere with radius {radius} is: {volume_of_sphere:.2f}")
