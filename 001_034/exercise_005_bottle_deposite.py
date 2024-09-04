"""
In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and two digits to the right of the decimal point.
"""

# Prompt the user to enter the count of small containers (1 liter or less)
num_small_containers = int(input("Enter the number of small containers (1 liter or less): "))

# Prompt the user to enter the count of large containers (more than 1 liter)
num_large_containers = int(input("Enter the number of large containers (more than 1 liter): "))

# Calculate the total refund based on the container sizes
total_refund = (num_small_containers * 0.10) + (num_large_containers * 0.25)

# Output the calculated refund, formatted to two decimal places with a dollar sign
print(f"Your total refund is: ${total_refund:.2f}")
