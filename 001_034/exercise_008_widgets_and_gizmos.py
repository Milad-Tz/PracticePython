"""
An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos from the user. Then your program should compute
and display the total weight of the parts.
"""
# Constants for the weights of each product
WIDGET_WEIGHT = 75  # weight of one widget in grams
GIZMO_WEIGHT = 112  # weight of one gizmo in grams

# Prompt the user to enter the number of widgets
num_widgets = int(input("Enter the number of widgets: "))

# Prompt the user to enter the number of gizmos
num_gizmos = int(input("Enter the number of gizmos: "))

# Calculate the total weight of the widgets and gizmos
total_weight = (num_widgets * WIDGET_WEIGHT) + (num_gizmos * GIZMO_WEIGHT)

# Display the total weight
print(f"The total weight of the products is: {total_weight} grams")
