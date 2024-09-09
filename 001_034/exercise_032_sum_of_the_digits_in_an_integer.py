"""
Develop a program that reads a four-digit integer from the user and displays the sum
of its digits. For example, if the user enters 3141 then your program should display
3 + 1 + 4 + 1 = 9.
"""

# Read a four-digit integer from the user
number = int(input("Enter a four-digit integer: "))

# Extract each digit using integer division and modulus
digit1 = number // 1000
digit2 = (number // 100) % 10
digit3 = (number // 10) % 10
digit4 = number % 10

# Calculate the sum of the digits
digit_sum = digit1 + digit2 + digit3 + digit4

# Display the result in the desired format
print(f"{digit1} + {digit2} + {digit3} + {digit4} = {digit_sum}")
