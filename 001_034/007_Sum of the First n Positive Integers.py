"""
Write a program that reads a positive integer, n, from the user and then displays the
sum of all the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula:
sum = (n)(n + 1) / 2
"""
# Read a positive integer from the user
n = int(input("Please enter a positive integer: "))

# Calculate the sum
sum_n = n * (n + 1) / 2

# Display the sum
print(f"The sum of the first {n} positive integers is: {sum_n}")
