"""
Write a program that begins by reading a temperature from the user in degrees Celsius.
Then your program should display the equivalent temperature in degrees Fahrenheit and degrees Kelvin.
The calculations needed to convert between different units of temperature can be found on the Internet.
"""

# Read the temperature from the user in degrees Celsius
celsius = float(input("Enter the temperature in degrees Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Convert Celsius to Kelvin
kelvin = celsius + 273.15

# Display the equivalent temperatures
print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}°F")
print(f"The temperature in Kelvin is: {kelvin:.2f}K")
