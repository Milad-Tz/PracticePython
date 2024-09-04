"""
The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places.
"""

# Reading the cost of the meal
cost = float(input("Please enter the cost of the meal ordered: "))

# Initialize parameters
tax_rate = 0.09
tip_rate = 0.18

# Calculate tax and tip
tax_amount = tax_rate * cost
tip_amount = tip_rate * cost

# Calculate grand total
grand_total = cost + tax_amount + tip_amount

# Display the results
print(f"The grand total is ${grand_total:.2f}")
print(f"The tax amount is ${tax_amount:.2f}")
print(f"The tip amount is ${tip_amount:.2f}")
