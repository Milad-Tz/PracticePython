"""
Consider the software that runs on a self-checkout machine. One task that it must be
able to perform is to determine how much change to provide when the shopper pays
for a purchase with cash.
Write a program that begins by reading a number of cents from the user as an
integer. Then your program should compute and display the denominations of the
coins that should be used to give that amount of change to the shopper. The change
should be given using as few coins as possible. Assume that the machine is loaded
with pennies, nickels, dimes, quarters, loonies and toonies.
"""
# Define the value of each coin in cents
TOONIE = 200   # 2-dollar coin
LOONIE = 100   # 1-dollar coin
QUARTER = 25   # 25-cent coin
DIME = 10      # 10-cent coin
NICKEL = 5     # 5-cent coin
PENNY = 1      # 1-cent coin

# Prompt the user to enter the amount of change in cents
cents = int(input("Enter the amount of change (in cents): "))

# Calculate the number of toonies (2-dollar coins)
num_toonies = cents // TOONIE
cents = cents % TOONIE  # Update the remaining cents

# Calculate the number of loonies (1-dollar coins)
num_loonies = cents // LOONIE
cents = cents % LOONIE  # Update the remaining cents

# Calculate the number of quarters (25-cent coins)
num_quarters = cents // QUARTER
cents = cents % QUARTER  # Update the remaining cents

# Calculate the number of dimes (10-cent coins)
num_dimes = cents // DIME
cents = cents % DIME  # Update the remaining cents

# Calculate the number of nickels (5-cent coins)
num_nickels = cents // NICKEL
cents = cents % NICKEL  # Update the remaining cents

# Calculate the number of pennies (1-cent coins)
num_pennies = cents // PENNY

# Display the result, showing how many of each coin is needed
print(f"Toonies (2-dollar coins): {num_toonies}")
print(f"Loonies (1-dollar coins): {num_loonies}")
print(f"Quarters (25-cent coins): {num_quarters}")
print(f"Dimes (10-cent coins): {num_dimes}")
print(f"Nickels (5-cent coins): {num_nickels}")
print(f"Pennies (1-cent coins): {num_pennies}")
