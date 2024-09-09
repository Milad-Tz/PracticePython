"""
In this exercise, you will create a program that reads a pressure from the user in kilopascals (kPa).
Once the pressure has been read, your program should report the equivalent pressure in
pounds per square inch (psi), millimeters of mercury (mmHg), and atmospheres (atm).
"""

# Conversion factors
KPA_TO_PSI = 0.145038
KPA_TO_MMHG = 7.50062
KPA_TO_ATM = 0.00986923

# Read the pressure from the user in kilopascals
kpa = float(input("Enter the pressure in kilopascals (kPa): "))

# Convert kilopascals to pounds per square inch (psi)
psi = kpa * KPA_TO_PSI

# Convert kilopascals to millimeters of mercury (mmHg)
mmhg = kpa * KPA_TO_MMHG

# Convert kilopascals to atmospheres (atm)
atm = kpa * KPA_TO_ATM

# Display the results
print(f"The pressure in pounds per square inch (psi): {psi:.2f}")
print(f"The pressure in millimeters of mercury (mmHg): {mmhg:.2f}")
print(f"The pressure in atmospheres (atm): {atm:.5f}")
