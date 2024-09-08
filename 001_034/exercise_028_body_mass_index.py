"""
Write a program that computes the body mass index (BMI) of an individual. Your
program should begin by reading a height and weight from the user. Then it should
use the following formula to compute the BMI before displaying it:
If you read the height in meters and the weight in kilograms, then the body mass index
is computed using this formula:
BMI = weight / (height × height)
"""

# Read height in meters from the user
height = float(input("Enter your height in meters: "))

# Read weight in kilograms from the user
weight = float(input("Enter your weight in kilograms: "))

# Compute the BMI using the metric formula
bmi = weight / (height ** 2)

# Display the calculated BMI
print(f"Your Body Mass Index (BMI) is: {bmi:.2f}")
