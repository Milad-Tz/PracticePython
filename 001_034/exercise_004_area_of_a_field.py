"""
Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres
"""
# Ask the user to enter the field width in feet
width = float(input("Enter the field width in feet: "))

# Ask the user to enter the field length in feet
length = float(input("Enter the field length in feet: "))

# Calculate the field area in square feet
area = width * length

# Convert the area to acres (1 acre = 43,560 square feet)
area_acres = area / 43560

# Display the area of the field in acres
print(f"The area of the field is: {area_acres:.4f} acres")
