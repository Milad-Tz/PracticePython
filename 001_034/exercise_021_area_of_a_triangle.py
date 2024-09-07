"""
The area of a triangle can be computed using the following formula, where b is the
length of the base of the triangle, and h is its height:

    area = (b × h) / 2

Write a program that allows the user to enter values for b and h. The program should
then compute and display the area of a triangle with base length b and height h.
"""
# Prompt the user to enter the base length of the triangle
base = float(input("Enter the base length of the triangle (in units): "))

# Prompt the user to enter the height of the triangle
height = float(input("Enter the height of the triangle (in units): "))

# Calculate the area of the triangle using the formula: area = (b × h) / 2
area = (base * height) / 2

# Display the result rounded to two decimal places
print(f"The area of the triangle is {area:.2f} square units.")
