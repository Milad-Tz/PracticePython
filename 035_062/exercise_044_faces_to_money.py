"""
It is common for images of a country’s previous leaders, or other individuals of historical significance, to appear on its money. The individuals that appear on banknotes in the United States are listed below:

Banknote Denomination | Individual
----------------------|--------------------
$1                    | George Washington
$2                    | Thomas Jefferson
$5                    | Abraham Lincoln
$10                   | Alexander Hamilton
$20                   | Andrew Jackson
$50                   | Ulysses S. Grant
$100                  | Benjamin Franklin

Write a program that begins by reading the denomination of a banknote from the user. Then your program should display the name of the individual that appears on the banknote of the entered amount. An appropriate error message should be displayed if no such note exists.

While two dollar banknotes are rarely seen in circulation in the United States, they are legal tender that can be spent just like any other denomination. The United States has also issued banknotes in denominations of $500, $1,000, $5,000, and $10,000 for public use. However, high denomination banknotes have not been printed since 1945 and were officially discontinued in 1969. As a result, we will not consider them in this exercise.
"""

# Read the denomination of the banknote from the user
denomination = int(input("Enter the denomination of the banknote (e.g., 1, 2, 5, 10, 20, 50, 100): "))

# Determine the individual that appears on the banknote of the entered denomination
if denomination == 1:
    individual = "George Washington"
elif denomination == 2:
    individual = "Thomas Jefferson"
elif denomination == 5:
    individual = "Abraham Lincoln"
elif denomination == 10:
    individual = "Alexander Hamilton"
elif denomination == 20:
    individual = "Andrew Jackson"
elif denomination == 50:
    individual = "Ulysses S. Grant"
elif denomination == 100:
    individual = "Benjamin Franklin"
else:
    individual = ""

# Display the result or an appropriate error message
if individual == "":
    print("There is no banknote of that denomination in the United States.")
else:
    print(f"The person on the ${denomination} bill is {individual}.")
