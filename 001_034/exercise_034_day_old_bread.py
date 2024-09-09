"""
A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
percent. Write a program that begins by reading the number of loaves of day-old
bread being purchased from the user. Then your program should display the regular
price for the bread, the discount because it is a day old, and the total price. Each of
these amounts should be displayed on its own line with an appropriate label.
All the values should be displayed using two decimal places, and the decimal points in
all the numbers should be aligned when reasonable values are entered by the user.
"""

# Define constants
LOAF_PRICE = 3.49  # Regular price per loaf
DISCOUNT_RATE = 0.60  # Discount rate for day-old bread

# Read the number of loaves from the user
num_loaves = int(input("Enter the number of day-old loaves: "))

# Calculate the regular price, discount, and total price
regular_price = num_loaves * LOAF_PRICE
discount = regular_price * DISCOUNT_RATE
total_price = regular_price - discount

# Display the results with proper formatting
print(f"Regular price:  ${regular_price:8.2f}")
print(f"Discount:      -${discount:8.2f}")
print(f"Total price:    ${total_price:8.2f}")
