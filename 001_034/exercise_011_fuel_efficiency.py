"""
In the United States, fuel efficiency for vehicles is normally expressed in
miles-per gallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
kilometers (L/100 km). Use your research skills to determine how to convert from
MPG to L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units.
"""
# Prompt the user to enter fuel efficiency in miles per gallon (MPG)
mpg = float(input("Enter fuel efficiency in miles per gallon (MPG): "))

# Convert MPG to liters per 100 kilometers (L/100 km) using the formula
l_per_100km = 235.215 / mpg

# Display the result rounded to 2 decimal places
print(f"The equivalent fuel efficiency in liters per 100 kilometers is: {l_per_100km:.2f} L/100 km")
