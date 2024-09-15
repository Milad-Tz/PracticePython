"""
Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message.
"""

# Prompt the user to enter the number of sides
sides = int(input("Enter the number of sides of the shape (between 3 and 10): "))

# Determine the shape based on the number of sides
if sides == 3:
    shape_name = "triangle"
elif sides == 4:
    shape_name = "quadrilateral"
elif sides == 5:
    shape_name = "pentagon"
elif sides == 6:
    shape_name = "hexagon"
elif sides == 7:
    shape_name = "heptagon"
elif sides == 8:
    shape_name = "octagon"
elif sides == 9:
    shape_name = "nonagon"
elif sides == 10:
    shape_name = "decagon"
else:
    shape_name = None

# Display the appropriate message
if shape_name:
    print(f"A shape with {sides} sides is called a {shape_name}.")
else:
    print("Error: Please enter a number of sides between 3 and 10.")
