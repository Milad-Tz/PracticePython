"""
Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10 a
• The result of a^b
"""
import math  # Importing math module for logarithmic function

# Read two integers from the user
a = int(input("Enter the first integer (a): "))
b = int(input("Enter the second integer (b): "))

# Compute and display the sum of a and b
sum_ab = a + b
print(f"The sum of {a} and {b} is: {sum_ab}")

# Compute and display the difference when b is subtracted from a
difference_ab = a - b
print(f"The difference when {b} is subtracted from {a} is: {difference_ab}")

# Compute and display the product of a and b
product_ab = a * b
print(f"The product of {a} and {b} is: {product_ab}")

# Compute and display the quotient when a is divided by b
if b != 0:
    quotient_ab = a / b
    print(f"The quotient when {a} is divided by {b} is: {quotient_ab:.2f}")
else:
    print("Division by zero is undefined.")

# Compute and display the remainder when a is divided by b
if b != 0:
    remainder_ab = a % b
    print(f"The remainder when {a} is divided by {b} is: {remainder_ab}")
else:
    print("Division by zero is undefined.")

# Compute and display the result of log10 a
if a > 0:
    log_a = math.log10(a)
    print(f"The result of log10({a}) is: {log_a:.2f}")
else:
    print("log10 is undefined for non-positive values.")

# Compute and display the result of a raised to the power of b
power_ab = a ** b
print(f"The result of {a} raised to the power of {b} (a^b) is: {power_ab}")
