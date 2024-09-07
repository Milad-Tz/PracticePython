"""
The amount of energy required to increase the temperature of one gram of a material
by one degree Celsius is the material’s specific heat capacity, C. The total amount
of energy, q, required to raise m grams of a material by ΔT degrees Celsius can be
computed using the formula:
q = mCΔT
Write a program that reads the mass of some water and the temperature change from
the user. Your program should display the total amount of energy that must be added
or removed to achieve the desired temperature change.
Hint: The specific heat capacity of water is 4.186 J/g◦C. Because water has a
density of 1.0 grams per milliliter, you can use grams and milliliters interchangeably in this exercise.
"""
# Define the specific heat capacity of water in J/g°C
SPECIFIC_HEAT_CAPACITY_WATER = 4.186  # J/g°C

# Prompt the user to enter the mass of water in grams (or milliliters, as they are equivalent)
mass = float(input("Enter the mass of water (in grams or milliliters): "))

# Prompt the user to enter the temperature change in degrees Celsius
temperature_change = float(input("Enter the temperature change (in degrees Celsius): "))

# Calculate the total energy required using the formula: q = m * C * ΔT
energy_required = mass * SPECIFIC_HEAT_CAPACITY_WATER * temperature_change

# Display the result
print(f"The total amount of energy required is {energy_required:.2f} Joules.")
